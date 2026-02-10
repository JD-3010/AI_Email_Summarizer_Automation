from gmail_reader import get_emails
from ai_news import get_ai_news
from weather import get_weather
from summarizer import format_message
from telegram_bot import send

emails = get_emails()[:20]  # Max 8 emails per run
ai_news = get_ai_news()
weather = get_weather("Coimbatore")

final_message = format_message(emails, ai_news, weather)

send(final_message)
