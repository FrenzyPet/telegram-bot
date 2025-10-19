import random
from telebot import types
from api.currency import getBtcPriceMessage


def register_commands(bot):
    @bot.message_handler(commands=["start"])
    def welcome(message):
        chat_id = message.chat.id
        welcome_text = """
🫡 Здравия желаю!

Я ваш верный цифровой товарищ. Я умею отвечать на интересующие вас вопросы.
        """
        bot.send_message(chat_id, welcome_text)

    @bot.message_handler(commands=["help"])
    def welcome(message):
        chat_id = message.chat.id
        help_text = """
Просто напишите мне сообщение с обращением ко мне на Frenzy, и я постараюсь помочь!

Например: "Frenzy, как построить цифровой коммунизм?"
        """
        bot.send_message(chat_id, help_text)

    @bot.message_handler(commands=["btc"])
    def btc(message: types.Message):
        text = getBtcPriceMessage()

        chat_id = message.chat.id
        bot.send_message(chat_id, text)
