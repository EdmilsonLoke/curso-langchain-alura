# Curso LangChain - Alura

Repositório criado para armazenar os projetos e exercícios desenvolvidos durante o curso de **LangChain e Python da Alura**.

Durante o curso, foram explorados conceitos relacionados ao desenvolvimento de aplicações utilizando modelos de linguagem (LLMs), incluindo criação de prompts, cadeias, histórico de conversas, LangGraph e RAG.

## 🧠 Conteúdos estudados

- Python aplicado a aplicações com IA
- LangChain
- Prompt Templates
- LCEL (LangChain Expression Language)
- Output Parsers
- Integração com Google Gemini
- Histórico de conversas
- RunnableWithMessageHistory
- LangGraph
- Fluxos e roteamento com grafos
- Embeddings
- Bancos vetoriais com FAISS
- RAG (Retrieval-Augmented Generation)
- Recuperação de informações em documentos
- Processamento de arquivos PDF

## 📂 Estrutura do projeto

### `main.py`

Exercícios iniciais utilizando LangChain e integração com modelos de linguagem.

### `main_chat.py`

Implementação de histórico de conversas utilizando LangChain.

### `main_langgraph.py`

Implementação de um fluxo de roteamento utilizando LangGraph.

### `main_rag.py`

Implementação de uma aplicação RAG utilizando documentos PDF, embeddings e FAISS.

### `documentos/`

Documentos utilizados como fonte de conhecimento para os experimentos com RAG.

### `requirements.txt`

Dependências utilizadas no projeto.

### `.gitignore`

Arquivos e diretórios que não devem ser enviados ao repositório, como o ambiente virtual e variáveis de ambiente.

## 🛠️ Tecnologias utilizadas

- Python
- LangChain
- LangGraph
- Google Gemini API
- FAISS
- Python-dotenv

## ⚙️ Configuração

Clone o repositório e instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do Google:

```env
GOOGLE_API_KEY=sua_chave_aqui
```

O arquivo `.env` não é enviado ao GitHub por estar incluído no `.gitignore`.

## 📚 Sobre o projeto

Este repositório representa minha evolução prática durante o estudo de desenvolvimento de aplicações com IA utilizando Python e o ecossistema LangChain.

O objetivo é manter os projetos como registro do aprendizado e também como referência para futuros projetos envolvendo inteligência artificial.
