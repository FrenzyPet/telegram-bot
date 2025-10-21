# Используем официальный Python-образ
FROM python:3.14-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё остальное
COPY . .

# Переменные окружения (чтобы не буферизовать вывод)
ENV PYTHONUNBUFFERED=1

# Команда запуска
CMD ["python", "bot.py"]