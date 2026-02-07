import json
from email_summarizer import summarize_and_categorize

def format_message(emails, ai_news, weather):
    categories = {
        "Jobs": [],
        "Bank": [],
        "Newsletters": [],
        "Miscellaneous": []
    }

    for i, mail in enumerate(emails, 1):
        print(f"Processing email {i}/{len(emails)}...")

        try:
            result = summarize_and_categorize(mail)

            data = json.loads(result)

            summary = data.get("summary", "Summary not available")
            cat = data.get("category", "Miscellaneous")

            if cat in categories:
                categories[cat].append(summary)
            else:
                categories["Miscellaneous"].append(summary)

        except Exception as e:
            categories["Miscellaneous"].append("Unable to summarize this email")

    msg = "🌅 Good Morning JD!\n\n"
    msg += "📬 Email Summary (Last 24 Hours)\n\n"

    icons = {
        "Jobs": "💼",
        "Bank": "🏦",
        "Newsletters": "📰",
        "Miscellaneous": "📦"
    }

    for cat, mails in categories.items():
        if mails:
            msg += f"{icons[cat]} {cat}:\n"
            for m in mails[:3]:
                msg += f"• {m}\n"
            msg += "\n"

    msg += "🧠 Top AI News Today:\n"
    for i, news in enumerate(ai_news, 1):
        msg += f"{i}. {news}\n"

    msg += f"""
🌦️ Weather Today (Coimbatore):
• Temperature: {weather['temp']}°C
• Condition: {weather['condition']}
• Humidity: {weather['rain']}%

Have a great day 🚀
"""

    return msg
