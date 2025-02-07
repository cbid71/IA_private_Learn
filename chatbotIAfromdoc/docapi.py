from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import OllamaEmbeddings
from langchain_postgres import PGVector
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, PromptTemplate
from langchain_ollama.llms import OllamaLLM


# Configure vector store
embeddings = OllamaEmbeddings(model="llama3.2", temperature=0.1)   # EMBEDDINGS temperature == after retrieval of data
vector_store = PGVector(
    embeddings=embeddings,
    collection_name="my_docs",
    connection="postgresql+psycopg://test:password@localhost:5432/mydb",
)

# Configure prompt and LLM
prompt = ChatPromptTemplate(
    input_variables=["context", "question"],
    messages=[
        HumanMessagePromptTemplate(
            prompt=PromptTemplate(
                input_variables=["context", "question"],
                template=(
                    "You are an assistant for question-answering tasks. Use the following pieces of retrieved "
                    #"context to answer the question. If you don't know the answer, just say that you don't know. "
                    "Context to answer the question. Fetch the answer from the vector store only, and if you do not know the answer, just say that you don't know. "
                    #"Use three sentences maximum and keep the answer concise.\n"
                    "Question: {question} \n"
                    "Context: {context} \n"
                    "Answer:"
                )
            )
        )
    ],
)

llm = OllamaLLM(model="llama3.2", temperature=0.2) # LLM temperature == creativity of generated response

# Retrieve relevant documents
def retrieve(question):
    retrieved_docs = vector_store.similarity_search(question)
    print(f"Retrieved {len(retrieved_docs)} documents.")
    for doc in retrieved_docs:
        print(f"Document: {doc.metadata}") 
        print(f"Document: {doc}")
    if not retrieved_docs:
        return [Document(page_content="No relevant documents found.")]
    return retrieved_docs

# Generate an answer
def generate(question):
    context = retrieve(question)
    docs_content = "\n\n".join(doc.page_content for doc in context)
    messages = prompt.invoke({"question": question, "context": docs_content}).to_messages()
    response = llm.invoke(messages)
    return response



# Declare a new API
app = FastAPI()

class SearchRequest(BaseModel):
    query: str

@app.post("/api/search")
async def search(request: SearchRequest):
    question = request.query
    answer = generate(question)
    print(f"Answer: {answer}")
    #return {"message": f"Vous avez recherché : {answer}"}
    return {"message": f"{answer}"}

# Pour lancer le serveur : uvicorn nom_du_fichier:app --reload

