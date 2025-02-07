
from langchain_ollama import OllamaEmbeddings
from langchain_postgres import PGVector

# une partie embeddings comme dependance au test du vector-store
embeddings = OllamaEmbeddings(model="llama3.2")
print (embeddings)

# le test le vector store
vector_store = PGVector(
    embeddings=embeddings,
    collection_name="my_docs",
    connection="postgresql+psycopg://test:password@localhost:5432/mydb",
)

print(vector_store)
