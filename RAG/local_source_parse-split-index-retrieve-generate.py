import bs4
import os

from langchain_community.document_loaders import UnstructuredMarkdownLoader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langgraph.graph import START, StateGraph
from typing_extensions import List, TypedDict
from pprint import pprint
from langchain.callbacks.tracers import ConsoleCallbackHandler


from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM
from langchain_postgres import PGVector

from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate

# Declare the embedding model, a dependency to create a new model
embeddings = OllamaEmbeddings(model="llama3.2")


# Declare the PGVector vector store
vector_store = PGVector(
    embeddings=embeddings,
    collection_name="my_docs",
    connection="postgresql+psycopg://test:password@localhost:5432/mydb",
)

# Load documentation
source_directory="/home/cyrille-biard/travail/keycloak/docs"

def load_markdown_files(directory):
    documents = []
    for root, _, files in os.walk(directory):  # Walk through all subdirectories
        for file in files:
            if file.endswith(".md"):  # Check for markdown files
                file_path = os.path.join(root, file)
                try:
                    loader = UnstructuredMarkdownLoader(file_path=file_path)
                    documents.extend(loader.load())  # Load and append documents
                except Exception as e:
                    print(f"Failed to parse {file_path}: {e}")
    return documents

docs = load_markdown_files(source_directory)

print(f"Total characters: {len(docs[0].page_content)}")

# Split the content in chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)

print(f"Split done : {len(all_splits)} sub-documents(also named chunks)")

# Index all chunks in the vector store
_ = vector_store.add_documents(documents=all_splits)

print("Chunks stored")


# Define prompt for question-answering
# -- Concept here, is to get a prompt template, that you will wrap in a humanmessageprompttemplate, to finally encapsulate in a chartprompttemplate
# -- The prompt template is a generic prompt which define the way the IA will behave to answer you
# -- The HumanMessagePromptTemplate is the level of prompt that will be used (it could be system template for example, but here we choose human message level
# ----- Each level of prompt has a dedicated work to be done //ADD THE VALUE OF EACH LEVEL
# -- Then we finally encapsulate the message template in a chatpromptTemplate which is the object led to manage the question 
individual_prompt = PromptTemplate(
    input_variables=["context", "question"],
    input_types={},
    partial_variables={},
    template=(
        "You are an assistant for question-answering tasks. Use the following pieces of retrieved "
        "context to answer the question. If you don't know the answer, just say that you don't know. "
        "Use three sentences maximum and keep the answer concise.\n"
        "Question: {question} \n"
        "Context: {context} \n"
        "Answer:"
    )
)

human_message_template = HumanMessagePromptTemplate(
    prompt=individual_prompt,
    additional_kwargs={}
)

prompt = ChatPromptTemplate(
    input_variables=["context", "question"],
    input_types={},
    partial_variables={},
    metadata={
        "owner": "Cyrille_Biard",
        "project": "MyFirstWork",
    },
    messages=[human_message_template]
)

# Define a state class, to manipulate the useful data for the application
class State(TypedDict):
    question: str
    context: List[Document]
    answer: str


# Define application steps, they will be used to format a context from known data (retrieve) then send a question and get the answer (generate)

llm = OllamaLLM(model="llama3.2")



# --- retrieve function will use the question, search in the vector store the useful parts of what has been fetched...
def retrieve(state: State):
    retrieved_docs = vector_store.similarity_search(state["question"])
    if not retrieved_docs:
      return {"context": [Document(page_content="No relevant documents found.")]}
    return {"context": retrieved_docs}

# --- generate function is later in this script configured to be chained after the retrieve function
# --- the generate function is meant to invoke an answer using question given by the user + context given by the retrieve function 
def generate(state: State):
    if not state["context"]:
        return {"answer": "Context is empty. Ensure 'retrieve' step returns valid data."}
    docs_content = "\n\n".join(doc.page_content for doc in state["context"])
    
    #messages = prompt.invoke({"question": state["question"], "context": docs_content}, config={'callbacks': [ConsoleCallbackHandler()]}).to_messages()
    messages = prompt.invoke({"question": state["question"], "context": docs_content}).to_messages()
    response = llm.invoke(messages)

    #return {"answer": messages[0].content}
    return {"answer": response}

# Compile application (aka retrieve) and test (aka generate)
graph_builder = StateGraph(State).add_sequence([retrieve, generate])
graph_builder.add_edge(START, "retrieve")
graph = graph_builder.compile()

print("Compilation done")

# Test the application
# --> invoke() will the functions retrieve and generate one after the other. 

#response = graph.invoke({"question": "What is Task Decomposition ?"})
#response = graph.invoke({"question": "what text are we talking about in your context ?"})
#response = graph.invoke({"question": "What is MIPS algorithms ? tell I don't know if you find nothing"})
#response = graph.invoke({"question": "What is the artical telling use about API-bank ?"})
#response = graph.invoke({"question": "Who is the author of the article ?"})
#response = graph.invoke({"question": "What is the artical telling us about LSH ?"})
#response = graph.invoke({"question": "What is the artical telling us about Locality-Sensitive Hashing ?"})
#response = graph.invoke({"question": "Are you really extracting your source from the article named  LLM Powered Autonomous Agents ?"})
#response = graph.invoke({"question": "Extract the informations about Self-Reflection from the article please, and focus on them"})

response = graph.invoke({"question": "Keycloack test with PostgreSQL ?"})

print ("QUESTION : ")
pprint(response['question'])
print ("CONTEXT : ")
pprint (response['context'])
print ("ANSWER : ")
print(response['answer'])

