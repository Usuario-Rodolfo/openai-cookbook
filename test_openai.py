import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
import asyncio

# Carrega as variáveis do .env
load_dotenv()

# Cria o cliente OpenAI com a chave do .env
client = AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Função de teste assíncrona
async def main():
    print("Cliente OpenAI configurado com sucesso!")
    # Aqui podes adicionar uma chamada de teste à API se quiseres
    # Exemplo:
    # response = await client.chat.completions.create(
    #     model="gpt-4.1-mini",
    #     messages=[{"role": "user", "content": "Olá, OpenAI!"}]
    # )
    # print(response.choices[0].message.content)

# Executa a função assíncrona
asyncio.run(main())