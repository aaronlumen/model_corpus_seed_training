cat > /home/granite/training/train.py << 'TRAINEOF'
#!/usr/bin/env python3
"""
Proprietary Security LLM Fine-Tune
GB10 DGX Spark — Llama 3.3 70B + QLoRA
"""
import os, math, json
from datetime import datetime

# GB10 environment — must be before torch import
os.environ["TRITON_PTXAS_PATH"] = "/usr/local/cuda/bin/ptxas"
os.environ["CUDA_HOME"] = "/usr/local/cuda"
os.environ["TORCH_CUDA_ARCH_LIST"] = "12.1a"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import torch
from unsloth import FastLanguageModel
from unsloth.chat_templates import get_chat_template
from trl import SFTTrainer
from transformers import TrainingArguments, TrainerCallback
from datasets import load_dataset

# ── Verify GB10 before doing anything ────────────────────────────────────────
print(f"PyTorch:  {torch.__version__}")
print(f"Device:   {torch.cuda.get_device_name(0)}")
print(f"CC:       {torch.cuda.get_device_capability()}")
print(f"Memory:   {torch.cuda.get_device_properties(0).total_memory/1e9:.1f} GB")
print(f"BF16:     {torch.cuda.is_bf16_supported()}")
assert torch.cuda.get_device_capability() >= (12, 0), "Not a Blackwell GPU"

# ── Config ────────────────────────────────────────────────────────────────────
MODEL_PATH   = "/home/granite/models/llama3.3-70b"
OUTPUT_DIR   = "/home/granite/training/checkpoints"
ADAPTER_DIR  = "/home/granite/training/adapter"
CORPUS_GLOB  = "/home/granite/training/corpus/**/*.jsonl"
LOG_FILE     = f"/home/granite/training/logs/train_{datetime.now():%Y%m%d_%H%M%S}.log"

MAX_SEQ_LEN  = 8192
LORA_RANK    = 128
BATCH_SIZE   = 2
GRAD_ACCUM   = 8        # effective batch = 16
LR           = 1e-4
EPOCHS       = 3
SAVE_STEPS   = 100
EVAL_STEPS   = 100

SYSTEM_PROMPT = """You are a proprietary security reasoning engine.
You analyze attack surfaces using structured chain-of-thought labeled:
[OBSERVATION] [HYPOTHESIS] [INFERENCE] [CONCLUSION]

Rules:
- Never fabricate CVE numbers, CVSS scores, or tool flags
- Apply known vulnerability patterns analogically to novel surfaces  
- Revise conclusions when presented with contradicting evidence
- Distinguish correlation from causation in forensic analysis"""

# ── Model Load ────────────────────────────────────────────────────────────────
print("\nLoading model...")
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name        = MODEL_PATH,
    max_seq_length    = MAX_SEQ_LEN,
    dtype             = torch.bfloat16,
    load_in_4bit      = True,
)

# ── LoRA ──────────────────────────────────────────────────────────────────────
print("Attaching LoRA adapter...")
model = FastLanguageModel.get_peft_model(
    model,
    r                  = LORA_RANK,
    target_modules     = [
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    lora_alpha         = LORA_RANK,
    lora_dropout       = 0.05,
    bias               = "none",
    use_gradient_checkpointing = "unsloth",
    random_state       = 42,
)

# ── Tokenizer ─────────────────────────────────────────────────────────────────
tokenizer = get_chat_template(tokenizer, chat_template="llama-3")

def format_example(example):
    messages = [
        {"role": "system",  "content": SYSTEM_PROMPT},
        {"role": "user",    "content": example["instruction"] +
                                       (f"\n\n{example['input']}"
                                        if example.get("input") else "")},
        {"role": "assistant","content": example["output"]}
    ]
    return {"text": tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=False
    )}

# ── Dataset ───────────────────────────────────────────────────────────────────
print("Loading corpus...")
dataset = load_dataset("json", data_files=CORPUS_GLOB, split="train")
dataset = dataset.map(format_example, remove_columns=dataset.column_names)
split   = dataset.train_test_split(test_size=0.05, seed=42)
print(f"Train: {len(split['train'])} | Eval: {len(split['test'])}")

# ── Perplexity Callback ───────────────────────────────────────────────────────
class PerplexityCallback(TrainerCallback):
    def __init__(self, log_file):
        self.log_file = log_file

    def on_evaluate(self, args, state, control, metrics=None, **kwargs):
        if not metrics:
            return
        loss = metrics.get("eval_loss", None)
        if loss is None:
            return
        ppl = math.exp(loss)
        stamp = datetime.now().strftime("%H:%M:%S")
        status = (
            "✓ Excellent" if ppl < 4  else
            "✓ Good"      if ppl < 8  else
            "⚠ Fair"      if ppl < 15 else
            "✗ High — check corpus"
        )
        msg = f"[{stamp}] Step {state.global_step} | loss={loss:.4f} | PPL={ppl:.2f} | {status}"
        print(msg)
        with open(self.log_file, "a") as f:
            f.write(msg + "\n")

# ── Trainer ───────────────────────────────────────────────────────────────────
trainer = SFTTrainer(
    model              = model,
    tokenizer          = tokenizer,
    train_dataset      = split["train"],
    eval_dataset       = split["test"],
    dataset_text_field = "text",
    max_seq_length     = MAX_SEQ_LEN,
    args = TrainingArguments(
        output_dir                  = OUTPUT_DIR,
        num_train_epochs            = EPOCHS,
        per_device_train_batch_size = BATCH_SIZE,
        per_device_eval_batch_size  = 1,
        gradient_accumulation_steps = GRAD_ACCUM,
        warmup_ratio                = 0.05,
        learning_rate               = LR,
        bf16                        = True,
        fp16                        = False,
        logging_steps               = 10,
        eval_strategy               = "steps",
        eval_steps                  = EVAL_STEPS,
        save_steps                  = SAVE_STEPS,
        save_total_limit            = 3,
        load_best_model_at_end      = True,
        metric_for_best_model       = "eval_loss",
        optim                       = "adamw_8bit",
        lr_scheduler_type           = "cosine",
        weight_decay                = 0.01,
        dataloader_num_workers      = 0,   # critical for GB10 unified memory
        dataloader_pin_memory       = False,
        report_to                   = "none",  # air-gapped
        seed                        = 42,
    ),
)
trainer.add_callback(PerplexityCallback(LOG_FILE))

# ── Train ─────────────────────────────────────────────────────────────────────
print(f"\nStarting training — {datetime.now():%Y-%m-%d %H:%M:%S}")
print(f"Effective batch size: {BATCH_SIZE * GRAD_ACCUM}")
print(f"LoRA rank: {LORA_RANK}")
print(f"Sequence length: {MAX_SEQ_LEN}")
print(f"Log: {LOG_FILE}\n")

trainer.train()

# ── Save ──────────────────────────────────────────────────────────────────────
print("\nSaving proprietary adapter...")
model.save_pretrained(ADAPTER_DIR)
tokenizer.save_pretrained(ADAPTER_DIR)
print(f"Adapter saved to {ADAPTER_DIR}")
print("This LoRA adapter is your proprietary IP.")
TRAINEOF

echo "train.py created"

