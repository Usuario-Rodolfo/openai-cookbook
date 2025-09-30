import os
import json
from openai import AsyncOpenAI
from dotenv import load_dotenv
import asyncio

# Carrega a chave do .env
load_dotenv()
client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Ficheiro para guardar histórico
HISTORY_FILE = "chat_history.json"

# Carrega histórico existente ou cria vazio
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        chat_history = json.load(f)
else:
    chat_history = []

async def chat():
    print("Chat com OpenAI (escreva 'sair' para terminar)")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break

        # Adiciona ao histórico
        chat_history.append({"role": "user", "content": user_input})

        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=chat_history
        )

        bot_message = response.choices[0].message["content"]
        print(f"OpenAI: {bot_message}")

        chat_history.append({"role": "assistant", "content": bot_message})

        # Salva o histórico
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(chat_history, f, ensure_ascii=False, indent=2)

asyncio.run(chat())
