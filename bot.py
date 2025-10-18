import random
import os
from telebot import TeleBot
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Получаем токен из переменной окружения
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Проверяем, что токен загружен
if not TOKEN:
    raise ValueError("Токен не найден! Проверьте файл .env")

bot = TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "Hello, i'am echo bot")


@bot.message_handler(func=lambda message: "hello" in message.text)
def greeting(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "hello")


@bot.message_handler(func=lambda message: True)
def tag_me(message):
    chat_id = message.chat.id
    current_user_id = message.from_user.id
    chat_member = bot.get_chat_member(chat_id, current_user_id)
    current_user = chat_member.user
    text = f"Случайный пользователь: @{current_user.username}"

    bot.send_message(chat_id, text)


bot.infinity_polling()
