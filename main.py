from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

numero_dias = 7
numero_criancas = 2
atividade = "musica"

prompt = f"Crie um roteiro de viagem de {numero_dias} dias, para uma familia com {numero_criancas} criancas, que gosta de {atividade}"

cliente = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key
)

resposta = cliente.invoke([
    ("system", "Voce é um assistente de roteiros de viagens."),
    ("human", prompt)
])

print(resposta.content)