import subprocess

def categorize(text):
    prompt = f"""
Classify this email into ONE category only:
Jobs
Bank
Newsletters
Miscellaneous

Email:
{text}

Respond with only the category name.
"""

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",     # ✅ FIX
        errors="ignore"       # ✅ SAFETY
    )

    return result.stdout.strip()
