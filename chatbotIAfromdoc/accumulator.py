import os
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_postgres import PGVector
from langchain_ollama import OllamaEmbeddings

# Configure embeddings and vector store
embeddings = OllamaEmbeddings(model="llama3.2")
vector_store = PGVector(
    embeddings=embeddings,
    collection_name="my_docs",
    connection="postgresql+psycopg://test:password@localhost:5432/mydb",
)

# Function to load markdown files
def load_markdown_files(directory):
    documents = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    loader = UnstructuredMarkdownLoader(file_path=file_path)
                    documents.extend(loader.load())
                except Exception as e:
                    print(f"Failed to parse {file_path}: {e}")
    return documents

# Main function
def main():
    source_directory = "/home/cyrille-biard/travail/Sources/RAG/keycloak/docs"
    docs = load_markdown_files(source_directory)
    print(f"Total documents loaded: {len(docs)}")
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
    chunks = text_splitter.split_documents(docs)
    print(f"Total chunks created: {len(chunks)}")
    
    vector_store.add_documents(documents=chunks)
    print("Chunks stored in the vector database.")

if __name__ == "__main__":
    main()
