# 🌟 AI-Powered Personal Email Assistant

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-LLM-purple?logo=data:image/png;base64,iVBORw0KGgo...)]()
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue?logo=telegram&logoColor=white)]()

---

![AI Email Assistant Flow](A_flowchart_infographic_illustrates_the_Automated_.png)

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

