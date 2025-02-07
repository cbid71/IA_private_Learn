
from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

# une partie embeddings comme dependance au test du vector-store
embeddings = OllamaEmbeddings(model="llama3.2")
print (embeddings)

# le test le vector store
vector_store = InMemoryVectorStore(embeddings)

print(vector_store)
