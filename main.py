from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "musica"

prompt = f"Crie um roteiro de viagem de {numero_dias} dias, para uma familia com {numero_criancas} criancas, que gosta de {atividade}"

cliente = OpenAI(api_key=api_key)

resposta = cliente.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role" : "system",
            "content" : "Voce é um assistente de roteiros de viagens."
        },
        {
            "role" : "user",
            "content" : prompt
        }
    ]
)

print(resposta)