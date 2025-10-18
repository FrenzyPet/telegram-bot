def register_commands(bot):
    @bot.message_handler(commands=["start"])
    def welcome(message):
        bot.reply_to(message, "Hello, i'am Frenzy Assistant")

    @bot.message_handler(commands=["pidor"])
    def pidor(message):
        chat_id = message.chat.id

        try:
            chat_members = []
            for member in bot.get_chat_administrators(chat_id):
                user = member.user

                if not user.is_bot:
                    chat_members.append(user)

            if not chat_members:
                bot.reply_to(message, "В чате нет участников 😢")
                return

            random_user = random.choice(chat_members)

            if random_user.username:
                user_tag = f"@{random_user.username}"
            else:
                user_tag = f"[{random_user.first_name}](tg://user?id={random_user.id})"

            bot.send_message(
                chat_id,
                f"Внимание всем! 🎯 Сегодня пидор: {user_tag}\n ❤️",
                parse_mode="Markdown",
            )

        except Exception as e:
            bot.reply_to(message, f"Ошибка: {e}")
