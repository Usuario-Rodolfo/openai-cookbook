import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import asyncio

# Carrega a chave do .env
load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")

# Inicializa o cliente
client = AsyncOpenAI(api_key=api_key)

# Histórico de conversas
history = []

async def chat():
    print("Chat com OpenAI (escreva 'sair' para terminar)")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break

        # Adiciona ao histórico
        history.append({"role": "user", "content": user_input})

        # Chama o modelo
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=history
        )

        # Pega a resposta do modelo
        reply = response.choices[0].message["content"]
        print(f"OpenAI: {reply}")

        # Adiciona resposta ao histórico
        history.append({"role": "assistant", "content": reply})

if __name__ == "__main__":
    asyncio.run(chat())