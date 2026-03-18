#!/usr/bin/env python3
"""
Export trained adapter to GGUF for Ollama deployment.
Run after training completes.
"""
import os, torch
os.environ["TRITON_PTXAS_PATH"] = "/usr/local/cuda/bin/ptxas"
os.environ["CUDA_HOME"] = "/usr/local/cuda"

from unsloth import FastLanguageModel

MODEL_PATH  = "/home/granite/models/llama3.3-70b"
ADAPTER_DIR = "/home/granite/training/adapter"
MERGED_DIR  = "/home/granite/training/merged"
GGUF_DIR    = "/home/granite/training/gguf"

print("Loading model + adapter for merge...")
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name     = ADAPTER_DIR,
    max_seq_length = 8192,
    dtype          = torch.bfloat16,
    load_in_4bit   = False,
)

# Merge LoRA into weights
print("Merging adapter → full weights (BF16)...")
model.save_pretrained_merged(MERGED_DIR, tokenizer, save_method="merged_16bit")
print(f"Merged model saved to {MERGED_DIR}")

# Export GGUF — Q8 because you have 128GB
print("Exporting to GGUF Q8_0...")
model.save_pretrained_gguf(GGUF_DIR, tokenizer, quantization_method="q8_0")
print(f"GGUF saved to {GGUF_DIR}")
print("\nNext: ollama create securityengine -f Modelfile")
