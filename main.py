from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

prompt_cidade = PromptTemplate(
    template="""
    Sugira uma cidade dado o meu interesse por {interesse}.
    """,
    input_variables=["interesse"]
)

modelo = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    temperature=0.5,
    api_key=api_key
)

cadeia = prompt_cidade | modelo | StrOutputParser()

resposta = cadeia.invoke(
    {
        "interesse" : "praias"
    }
)
print(resposta)