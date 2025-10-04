import os
import openai

# Carrega a chave da variável de ambiente
openai.api_key = os.environ.get("OPENAI_API_KEY")

if openai.api_key:
    print("✅ A chave da OpenAI foi carregada corretamente no Codespace!")
else:
    print("❌ A chave da OpenAI não foi encontrada no Codespace.")
