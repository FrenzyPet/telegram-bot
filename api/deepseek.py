from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=DEEPSEEK_API_KEY,
)


def get_deepseek_answer(prompt, system_message=None, temperature=0.7, max_tokens=2000):
    # Базовый системный промпт для улучшения качества ответов
    if system_message is None:
        system_message = """Ты - полезный AI-ассистент. Отвечай точно на вопрос, 
        будь информативным и структурированным. Используй русский язык для ответов."""

    messages = []

    # Добавляем системное сообщение для настройки поведения модели
    if system_message:
        messages.append({"role": "system", "content": system_message})

    # Добавляем пользовательский запрос
    messages.append({"role": "user", "content": prompt})

    try:
        completion = client.chat.completions.create(
            model="alibaba/tongyi-deepresearch-30b-a3b:free",
            messages=messages,
            temperature=temperature,  # Контроль креативности (0-1)
            max_tokens=max_tokens,  # Ограничение длины ответа
            stream=False,
        )

        answer = completion.choices[0].message.content
        return answer.strip()

    except Exception as e:
        return f"Ошибка при получении ответа: {str(e)}"
