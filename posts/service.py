import os

from telegram import Bot


def send_telegram_message(chat_id, message):
    bot = Bot(token=os.getenv('TG_TOKEN'))
    bot.send_message(chat_id=chat_id, text=message)
