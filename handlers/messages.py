HELLO_MESSAGES = [
    "hello",
    "hi",
    "привет",
    "здравствуй",
    "хай",
    "дороу",
    "здарова",
    "дарова",
    "здравия желаю",
]

SALAM_MESSAGES = ["салам", "салам алейкум", "салям алейкум"]


def register_message_handlers(bot):
    @bot.message_handler(
        func=lambda message: any(
            hello_word in message.text.lower() for hello_word in HELLO_MESSAGES
        )
    )
    def greeting(message):
        bot.send_message(message.chat.id, "здравия желаю 🫡")

    @bot.message_handler(
        func=lambda message: any(
            hello_word in message.text.lower() for hello_word in SALAM_MESSAGES
        )
    )
    def salam(message):
        bot.send_message(
            message.chat.id,
            """привет! шучу - ваалейкум ассалам ☝🏽""",
        )
