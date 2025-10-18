import os
from telebot import TeleBot, types
from dotenv import load_dotenv

from handlers.commands import register_commands
from handlers.messages import register_message_handlers

load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Токен не найден! Проверьте файл .env")

bot = TeleBot(TOKEN)


register_commands(bot)
register_message_handlers(bot)


if __name__ == "__main__":
    bot.infinity_polling()
