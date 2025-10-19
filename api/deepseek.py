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


def getDeepseekAnswer(prompt):
    request = prompt + ". Отвечай на русском языке"
    completion = client.chat.completions.create(
        model="alibaba/tongyi-deepresearch-30b-a3b:free",
        messages=[{"role": "user", "content": prompt}],
        stream=False,
    )

    answer = completion.choices[0].message.content

    return answer
