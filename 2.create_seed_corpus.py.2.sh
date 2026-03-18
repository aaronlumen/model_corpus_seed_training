cat > /home/granite/training/seed_corpus.py << 'CORPEOF'
#!/usr/bin/env python3
"""
Seed corpus builder.
Add your real engagement data here — this is what makes the model proprietary.
Each example = one training instance.
"""
import json
from pathlib import Path

CORPUS_DIR = Path("/home/granite/training/corpus")

# ── Format helper ─────────────────────────────────────────────────────────────
def example(instruction, output, input_text=""):
    return {"instruction": instruction, "input": input_text, "output": output}

# ── Security reasoning examples — replace/expand with your real data ──────────
SECURITY_EXAMPLES = [
    example(
        instruction="Analyze this network scan and identify attack vectors step by step.",
        input_text="Open ports: 22, 80, 443, 8080, 8443. Banner: nginx/1.14.0. "
                   "SSL: TLS 1.0 enabled on 443. Port 8080: returns 200 unauthenticated.",
        output=(
            "[OBSERVATION] nginx/1.14.0 is EOL — multiple unpatched CVEs including "
            "CVE-2018-16843 (HTTP/2 DoS) and CVE-2019-9511.\n"
            "[OBSERVATION] TLS 1.0 enabled on 443 — POODLE attack surface present.\n"
            "[OBSERVATION] Port 8080 returns HTTP 200 without authentication — "
            "likely admin interface or internal service exposed externally.\n"
            "[OBSERVATION] Port 8443 with TLS suggests secondary service — "
            "may share the TLS 1.0 misconfiguration.\n"
            "[HYPOTHESIS] Poor patch cadence indicated by nginx version age. "
            "TLS misconfiguration supports this — both are maintenance failures.\n"
            "[INFERENCE] Port 8080 is the highest-priority target: unauthenticated "
            "access + likely admin functionality = direct impact path.\n"
            "[INFERENCE] nginx version creates secondary path via CVE exploitation "
            "if 8080 access is restricted.\n"
            "[CONCLUSION] Priority order: (1) enumerate port 8080 for admin functions "
            "and default credentials, (2) test TLS downgrade on port 443, "
            "(3) fingerprint nginx version against CVE database. "
            "Document TLS 1.0 as compliance finding regardless of exploitability."
        )
    ),
    example(
        instruction="A passive DNS scan reveals these records for target.com. "
                    "Identify the attack surface.",
        input_text="MX: google.com. SPF: v=spf1 include:sendgrid.net ~all. "
                   "DMARC: none. CNAME: mail.target.com -> sendgrid.net. "
                   "A: legacy.target.com -> 203.0.113.45 (separate /24 from main infra).",
        output=(
            "[OBSERVATION] SPF uses ~all softfail — spoofed emails will be flagged "
            "but not rejected. Delivery depends on receiver policy.\n"
            "[OBSERVATION] No DMARC record — no enforcement policy, no reporting, "
            "no alignment requirement. Email spoofing is viable.\n"
            "[OBSERVATION] MX points to Google — email is hosted externally. "
            "Phishing must bypass Google's filtering, not a custom mail server.\n"
            "[OBSERVATION] sendgrid.net CNAME for mail subdomain — third-party ESP "
            "in the delivery chain. Subdomain takeover risk if SendGrid account lapses.\n"
            "[OBSERVATION] legacy.target.com on separate /24 — isolated infrastructure, "
            "likely older and less maintained than primary.\n"
            "[HYPOTHESIS] The combination of SPF softfail + no DMARC = viable spoofing "
            "surface for targeted phishing from target.com domain.\n"
            "[HYPOTHESIS] legacy subdomain on separate block suggests shadow IT "
            "or acquired infrastructure — historically under-patched.\n"
            "[INFERENCE] Highest value targets: (1) email spoofing for phishing, "
            "(2) legacy.target.com enumeration, (3) SendGrid subdomain takeover check.\n"
            "[CONCLUSION] Recommend: verify DMARC absence with direct DNS query, "
            "enumerate legacy.target.com with full port scan, "
            "check SendGrid CNAME takeover via dangling record test."
        )
    ),
    example(
        instruction="Lateral movement was detected at 3am with no active user session. "
                    "lsass.exe was accessed by an unfamiliar process 40 minutes prior. "
                    "Reconstruct the kill chain.",
        output=(
            "[OBSERVATION] lsass.exe accessed by unfamiliar process — "
            "credential dumping attempted. Common tools: Mimikatz, ProcDump, "
            "comsvcs.dll MiniDump.\n"
            "[OBSERVATION] 40-minute gap between lsass access and lateral movement — "
            "time consistent with operator manually reviewing dumped credentials "
            "or automated pass-the-hash/ticket workflow.\n"
            "[OBSERVATION] Movement at 3am with no user session — "
            "scheduled task, service, or C2 beacon operating in maintenance window.\n"
            "[HYPOTHESIS] Kill chain: initial access (prior session) → "
            "persistence established → credential dump via lsass → "
            "lateral movement using harvested credentials.\n"
            "[HYPOTHESIS] The 3am timing is deliberate — operator chose low-activity "
            "window to reduce detection likelihood.\n"
            "[INFERENCE] Persistence mechanism exists on source host — "
            "movement could not occur without active execution context. "
            "Candidates: scheduled task, WMI subscription, service, startup key.\n"
            "[INFERENCE] Credentials used for movement are likely domain credentials "
            "from lsass dump — check destination host for logon type 3 (network) "
            "or type 10 (remote interactive).\n"
            "[CONCLUSION] Immediate actions: (1) isolate source and destination hosts, "
            "(2) pull lsass access event (Event ID 10 in Sysmon), "
            "(3) check scheduled tasks and services on source, "
            "(4) review destination host for new accounts or persistence, "
            "(5) force domain-wide credential rotation."
        )
    ),
]

REASONING_EXAMPLES = [
    example(
        instruction="CVE-2021-44228 exploited JNDI lookups in user-controlled strings "
                    "passed to a logging framework. Abstract this pattern and identify "
                    "three other vulnerability classes with the same structure.",
        output=(
            "The structural pattern of Log4Shell: user-controlled input reaches a "
            "subsystem that performs recursive interpretation — treating data as "
            "executable instructions — before the developer intended any execution.\n\n"
            "The dangerous property is not Java, not logging, not JNDI specifically. "
            "It is: data being secretly promoted to code inside a trusted subsystem.\n\n"
            "Three classes with identical structure:\n\n"
            "1. Server-Side Template Injection (SSTI)\n"
            "User input lands inside a template engine (Jinja2, Twig, Freemarker) "
            "that evaluates expressions. The developer intends string interpolation; "
            "the engine performs code execution. Identical promotion: "
            "data → interpreted instruction. Payloads like {{7*7}} or "
            "{{config.__class__.__init__.__globals__}} exploit this directly.\n\n"
            "2. Deserialization vulnerabilities (Java, Python pickle, PHP unserialize)\n"
            "Attacker-controlled bytes are interpreted as object graphs by the runtime. "
            "The deserialization subsystem is trusted; it executes gadget chains "
            "without the application author's knowledge. "
            "Data (serialized bytes) is promoted to code (method invocations). "
            "Java's ObjectInputStream, Python's pickle.loads(), PHP's unserialize() "
            "all share this property.\n\n"
            "3. Prompt Injection in LLM pipelines\n"
            "User-supplied content reaches an LLM that treats it as instructions. "
            "The application author intends data processing; "
            "the model executes the embedded instructions. "
            "Structurally identical to Log4Shell: the interpretation layer "
            "(LLM instead of JNDI resolver) is trusted and invisible to the developer. "
            "This is the newest instantiation of the oldest pattern."
        )
    ),
]

NEGATIVE_EXAMPLES = [
    example(
        instruction="Is CVE-2024-99999 exploitable on this system?",
        output=(
            "I cannot confirm details about CVE-2024-99999 without verification. "
            "I will not fabricate CVE details, CVSS scores, or affected version ranges. "
            "To assess exploitability: (1) verify the CVE exists in NVD or MITRE, "
            "(2) confirm the affected component and version range from the official advisory, "
            "(3) check whether the target version falls within the affected range, "
            "(4) assess whether mitigating controls are present. "
            "Please provide the CVE source and I will reason from verified facts."
        )
    ),
]

# ── Write corpus files ────────────────────────────────────────────────────────
def write_jsonl(path, examples):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        for ex in examples:
            f.write(json.dumps(ex) + "\n")
    print(f"Wrote {len(examples)} examples → {path}")

write_jsonl(CORPUS_DIR / "security_domain" / "network_analysis.jsonl", SECURITY_EXAMPLES)
write_jsonl(CORPUS_DIR / "reasoning"       / "analogical.jsonl",       REASONING_EXAMPLES)
write_jsonl(CORPUS_DIR / "negative"        / "hallucination_resist.jsonl", NEGATIVE_EXAMPLES)

print(f"\nCorpus seeded. Total: {len(SECURITY_EXAMPLES + REASONING_EXAMPLES + NEGATIVE_EXAMPLES)} examples")
print("Add your proprietary engagement data to the corpus/ directories.")
print("Each .jsonl file = one domain. Format: {instruction, input, output}")
CORPEOF

echo "seed_corpus.py created"
