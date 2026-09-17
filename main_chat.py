from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

modelo = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.5,
    api_key=api_key
)

lista_perguntas = [
    "Quero visitar um lugar no Brasil, famoso por praias e culturas. Pode sugerir?",
    "Qual a melhor epoca do ano para ir?"
]

for uma_pergunta in lista_perguntas:
    resposta = modelo.invoke(uma_pergunta)
    print("Usuario: ", uma_pergunta)
    print("IA: ", resposta.content, "\n")
