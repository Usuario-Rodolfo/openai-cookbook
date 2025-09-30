import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega a chave do .env
load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Faz uma chamada de teste ao modelo
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Escreve uma frase curta motivacional."}
    ]
)

# Mostra a resposta
print(response.choices[0].message.content)