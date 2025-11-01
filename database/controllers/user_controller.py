from sqlalchemy.orm import Session
from ..connection import engine
from ..models import User
import uuid


class UserController:
    """Контроллер для работы с пользователями"""

    def get_user_by_telegram_id(self, user_id: str) -> User:
        """Находит пользователя по Telegram ID"""
        with Session(engine) as session:
            user = session.query(User).filter(User.user_id == user_id).first()
            return user

    def create_user(self, user_id: str, first_name: str) -> User:
        """Создает нового пользователя (если еще не существует)"""
        # Сначала проверяем есть ли пользователь
        existing_user = self.get_user_by_telegram_id(user_id)
        if existing_user:
            print(f"✅ Пользователь уже существует: {first_name} (ID: {user_id})")
            return existing_user

        # Если нет - создаем нового
        with Session(engine) as session:
            user = User(
                id=str(uuid.uuid4()), user_id=str(user_id), first_name=first_name
            )
            session.add(user)
            session.commit()
            print(f"✅ Создан новый пользователь: {first_name} (ID: {user_id})")
            return user
