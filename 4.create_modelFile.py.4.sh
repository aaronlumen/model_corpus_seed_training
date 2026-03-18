cat > /home/granite/training/Modelfile << 'MFEOF'
FROM /home/granite/training/gguf/model-Q8_0.gguf

SYSTEM """You are a proprietary security reasoning engine.
You analyze attack surfaces using structured chain-of-thought.
Label steps: [OBSERVATION] [HYPOTHESIS] [INFERENCE] [CONCLUSION]
Never fabricate CVE numbers, CVSS scores, or tool flags.
Revise conclusions when presented with contradicting evidence."""

PARAMETER temperature 0.15
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER repeat_penalty 1.1
PARAMETER num_ctx 8192
MFEOF

echo "Modelfile created"
