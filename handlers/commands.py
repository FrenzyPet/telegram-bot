import random
from telebot import types
from api.currency import getBtcPriceMessage


def register_commands(bot):
    @bot.message_handler(commands=["start"])
    def welcome(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Hello, i'am Frenzy Assistant")

    @bot.message_handler(commands=["btc"])
    def btc(message: types.Message):
        text = getBtcPriceMessage()

        chat_id = message.chat.id
        bot.send_message(chat_id, text)
