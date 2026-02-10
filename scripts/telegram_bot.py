import asyncio
from telegram import Bot

BOT_TOKEN = "BOT_ID"
CHAT_ID = "User_ID"

MAX_LEN = 4000

async def _send_async(msg):
    bot = Bot(token=BOT_TOKEN)
    for i in range(0, len(msg), MAX_LEN):
        await bot.send_message(
            chat_id=CHAT_ID,
            text=msg[i:i + MAX_LEN]
        )

def send(msg):
    asyncio.run(_send_async(msg))
