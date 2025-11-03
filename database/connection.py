import os
from sqlalchemy import create_engine
from .models import Base


def get_database_url():
    """Возвращает URL для подключения к БД в зависимости от окружения"""
    if os.getenv("DATABASE_URL"):
        return os.getenv("DATABASE_URL")

    return "postgresql://bot_user:bot_pass@localhost:5432/bot_db"


print("🔄 Подключаюсь к базе данных...")

db_url = get_database_url()
engine = create_engine(db_url)

Base.metadata.create_all(engine)

print("✅ База данных подключена!")
print("✅ Таблицы созданы!")
print(f"📍 PostgreSQL: {db_url}")
