from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

modelo = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.5,
    api_key=api_key
)

prompt_consultor = ChatPromptTemplate.from_messages(
    [
        ("system", "Voce é um consultor de viagens"),
        ("human", "{query}")
    ]
)

assistente = prompt_consultor | modelo | StrOutputParser()

print(assistente.invoke({"query": "Quero ferias em praias do Brasil."}))