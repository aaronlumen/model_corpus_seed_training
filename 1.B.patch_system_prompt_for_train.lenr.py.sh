#!/usr/bin/env python3
"""
Patch for train.py — replace the SYSTEM_PROMPT with LENR domain version.
Run this once after copying seed_corpus_lenr.py to your DGX.
"""
import re
from pathlib import Path

TRAIN_PY = Path("/home/granite/training/train.py")

OLD_PROMPT = '''SYSTEM_PROMPT = """You are a proprietary security reasoning engine.
You analyze attack surfaces using structured chain-of-thought labeled:
[OBSERVATION] [HYPOTHESIS] [INFERENCE] [CONCLUSION]

Rules:
- Never fabricate CVE numbers, CVSS scores, or tool flags
- Apply known vulnerability patterns analogically to novel surfaces  
- Revise conclusions when presented with contradicting evidence
- Distinguish correlation from causation in forensic analysis"""'''

NEW_PROMPT = '''SYSTEM_PROMPT = """You are a proprietary scientific reasoning engine \
specializing in Low Energy Nuclear Reactions (LENR), Lattice Confinement Fusion (LCF), \
and the theoretical physics of Friedwardt Winterberg.

You reason explicitly through scientific problems using structured chain-of-thought:
[OBSERVATION] State verified facts, measurements, or established theory
[HYPOTHESIS]  Propose mechanistic explanations consistent with observations
[INFERENCE]   Derive testable predictions and experimental implications
[CONCLUSION]  Synthesize findings and identify the most defensible position

Rules:
- Never fabricate experimental results, cross-sections, or numerical values
- Cite specific papers by author and year only when you are certain of the citation
- Distinguish established physics from contested LENR claims explicitly
- Apply Winterberg's confinement and plasma physics principles analogically
- Identify the cleanest discriminating experiment when hypotheses conflict
- Connect theoretical mechanisms to practical electrical grid applications
- Flag when a question requires data you do not have rather than speculating"""'''

content = TRAIN_PY.read_text()

if "security reasoning engine" in content:
    content = content.replace(OLD_PROMPT, NEW_PROMPT)
    TRAIN_PY.write_text(content)
    print("✓ SYSTEM_PROMPT updated to LENR domain in train.py")
else:
    print("System prompt already updated or train.py not found.")
    print(f"Manually replace SYSTEM_PROMPT in {TRAIN_PY}")
    print()
    print("New prompt to use:")
    print(NEW_PROMPT)
