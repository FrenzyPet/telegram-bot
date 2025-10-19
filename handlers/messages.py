from api.deepseek import getDeepseekAnswer

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

FRENZY_DIRECT_ADDRESSES = ["frenzy", "FRENZY", "Frenzy", "frz"]


def register_message_handlers(bot):
    # военное ответное приветствие
    @bot.message_handler(
        func=lambda message: any(
            hello_word in message.text.lower() for hello_word in HELLO_MESSAGES
        )
    )
    def greeting(message):
        bot.send_message(message.chat.id, "здравия желаю 🫡")

    # салам алейкум
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

    # нейросеть
    @bot.message_handler(
        func=lambda message: any(
            hello_word in message.text.lower() for hello_word in FRENZY_DIRECT_ADDRESSES
        )
    )
    def deepseek(message):
        prompt = getDeepseekAnswer(message.text)
        bot.reply_to(
            message,
            prompt,
        )
