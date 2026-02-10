# 🌟 AI-Powered Personal Email Assistant

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-LLM-purple?logo=data:image/png;base64,iVBORw0KGgo...)]()
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram&logoColor=white)]()
---
#### Do Connect through LinkedIn : www.linkedin.com/in/jeremy-david-643870201/
---

## 📝 Project Description

This project is a **local AI-powered email assistant** that:

- Reads your Gmail securely (read-only)
- Summarizes emails using a **locally running LLM (Ollama + LLaMA)**
- Categorizes emails into:
  - 💼 Jobs
  - 🏦 Bank
  - 📰 Newsletters
  - 📦 Miscellaneous
- Sends a **daily morning briefing to Telegram**
- Adds **Top AI News** and **Weather Reports**

**Privacy-first:** All data processing is local. No emails leave your laptop.

---

## ⚡ Features

| Feature | Description |
|---------|-------------|
| Gmail OAuth | Secure read-only access with `token.json` handling |
| Local AI Summarization | Ollama + LLaMA models process emails locally |
| Categorization | Jobs / Bank / Newsletters / Miscellaneous |
| Daily Telegram Message | Summarized emails sent automatically |
| AI News | Top 5 AI news fetched from RSS feeds |
| Weather Info | Current weather for your city from free APIs |
| Modular Design | Separate scripts for email, AI, telegram, news, weather |

---

## 🛠 Tools & Technologies

| Category | Tools / Libraries |
|----------|-----------------|
| Programming Language | Python 3.11.x |
| LLM | Ollama (LLaMA 3 / 3:8B) |
| APIs | Gmail API, Telegram Bot API, RSS feeds, wttr.in |
| Python Libraries | google-api-python-client, google-auth, google-auth-oauthlib, python-telegram-bot, requests, feedparser |
| IDE | VS Code |

---

## 📂 Folder Structure

Email_ai_assistant/
│
├── main.py # Entry point
├── gmail_reader.py # Gmail OAuth & fetching emails
├── email_summarizer.py # Local AI summarization & categorization
├── summarizer.py # Formats final Telegram message
├── telegram_bot.py # Sends messages to Telegram
├── ai_news.py # Fetches AI news via RSS
├── weather.py # Fetches weather info
│
├── credentials.json # Google OAuth credentials
├── token.json # Auto-generated token (first login)
├── requirements.txt # Python dependencies
├── README.md # Project documentation

---

## ▶️ Execution Flow

```
Start Program
   ↓
Gmail OAuth Check
   ↓
Fetch Latest Emails
   ↓
AI Summarization (Local)
   ↓
Email Categorization
   ↓
Fetch AI News
   ↓
Fetch Weather
   ↓
Format Message
   ↓
Send to Telegram
   ↓
End 
```
---

## 📬 Sample Output

```
🌅 Good Morning JD!

📬 Email Summary (Last 24 Hours)

💼 Jobs:
• Amazon interview scheduled on Feb 8 at 11 AM via Zoom. Action required.

🏦 Bank:
• HDFC credit card bill ₹3,240 due on Feb 10. Payment required.

📰 Newsletters:
• Analytics Vidhya shares top data trends for 2026. No action required.

📦 Miscellaneous:
• Amazon order delivered successfully. No action required.

🧠 Top AI News Today:
1. OpenAI improves reasoning models
2. Google Gemini expands context window
3. Microsoft adds AI features to Excel
4. Meta open-sources new LLM tools
5. AI hiring tools adoption rises

🌦️ Weather Today (Coimbatore):
• Temperature: 29°C
• Condition: Partly Cloudy
• Humidity: 65%

Have a great day 🚀
```

---
## 🔧 How It Works

- Program starts and checks for Gmail OAuth token
- Fetches the latest emails (last N emails)
- Each email is summarized using Ollama locally
- Emails are categorized into:

  Jobs
  Bank
  Newsletters
  Miscellaneous

- Latest AI news is fetched via RSS feeds
- Weather information is fetched from a free public API
- The summary message is formatted with emojis for clarity
- Telegram Bot sends the final formatted message

---

## 🚀 Future Enhancements

- Schedule daily execution using Task Scheduler (Windows) or cron (Linux)
- Highlight urgent or action-required emails at the top
- Cache previous email summaries to reduce repeated AI processing
- Dockerized deployment for cross-platform availability
- WhatsApp integration for additional notifications
- Extract events or reminders for calendar integration

---

## 📌 Conclusion

This project demonstrates how to combine local AI (Ollama + LLaMA) with real-world automation:

- Automates reading, summarizing, and categorizing emails
- Delivers a concise, daily briefing to Telegram
- Includes AI news and weather updates
- Fully local, privacy-first, and modular for expansion

