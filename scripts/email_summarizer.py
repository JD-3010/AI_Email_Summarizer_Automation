import subprocess

def summarize_and_categorize(text):
    prompt = f"""
You are an assistant that summarizes emails for a daily personal briefing.

TASK:
1. Write a clear, factual summary in **1–2 short lines**
2. Classify the email into ONE category:
   Jobs / Bank / Newsletters / Miscellaneous

STRICT RULES:
- Do NOT include greetings, signatures, or legal footers
- Do NOT invent information
- If no action is required, explicitly say "No action required"
- If dates, money, or deadlines exist, mention them
- Keep summary under 25 words
- Neutral, professional tone

Start the summary with:
- [URGENT] : if action is required within 48 hours
- [ACTION] : if action required but no deadline
- [INFO] : if informational only

OUTPUT FORMAT (JSON ONLY):
{{
  "summary": "<short summary>",
  "category": "<one category>"
}}

Email:
{text}
"""

    result = subprocess.run(
        ["ollama", "run", "llama3", prompt],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="ignore"
    )

    return result.stdout.strip()
