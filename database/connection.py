from sqlalchemy import create_engine
import os
from .models import Base  # импортируем Base и модели

print("🔄 Подключаюсь к базе данных...")

# Создаем путь к БД внутри папки database
db_path = os.path.join(os.path.dirname(__file__), "bot_database.db")
engine = create_engine(f"sqlite:///{db_path}")

# Создаем таблицы
Base.metadata.create_all(engine)

print("✅ База данных подключена!")
print("✅ Таблицы созданы!")
print(f"📍 Файл: {db_path}")
