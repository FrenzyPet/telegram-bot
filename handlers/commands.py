import random
from telebot import types
from api.currency import getBtcPriceMessage
from database.controllers.user_controller import UserController


def register_commands(bot):
    @bot.message_handler(commands=["start"])
    def welcome(message):
        chat_id = message.chat.id

        user_controller = UserController()
        user = user_controller.create_user(
            user_id=str(message.from_user.id), first_name=message.from_user.first_name
        )

        # Разные сообщения для нового и существующего пользователя
        if user_controller.get_user_by_telegram_id(str(message.from_user.id)):
            welcome_text = f"""
    🫡 С возвращением, {message.from_user.first_name}!

    Рад снова тебя видеть, товарищ!
            """
        else:
            welcome_text = f"""
    🫡 Здравия желаю, {message.from_user.first_name}!

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
