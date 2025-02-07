import getpass
import os

if not os.environ.get("OLLAMA_API_KEY"):
    os.environ["OLLAMA_API_KEY"] = getpass.getpass("Enter API key for Ollama: ")

from langchain_ollama import ChatOllama  # Module for Ollama

# Configuration du modèle Ollama 3.2
llm = ChatOllama(model="ollama/3.2")


print (llm)
