# Best practices

https://github.com/DataTalksClub/llm-zoomcamp/tree/main/06-best-practices

## tips and tricks for advanced RAG system

### What is a RAG ?

![What is RAG](what_is_RAG.png)

### How to accumulate data ?

Parse initial documents -> Cut in chunks (then in token) -> calculate vectors -> store vectors in a database

### For the machine to answer ?

Turn the question into a vector form -> extract top K documents related to those vectors -> Show your question and the relevant documents to your LLM -> fetch the result from the LLM
Of course you can use the LLM to select the best vectors related to your question.

## How to improve the retrieval (choose of best documents) step ?

** Method 1 : ** Choose the right chunk size

Use small chunks on embedding stage and large chunks on answering stage

** Method 2 : ** Metadata
 - Add metadata on your documents before chucking
 - Add LLM to produce the metadata 
Example of metadata : document path, document name

Note : See the file named `about_improving_retrieval_by_adding_metadata.md` for more explaination.

** Method 3 : ** Hybrid approach 

 - Vector based search and keyword based search in a pipeline
 - Vector search is looking the closest chunks in the database (semantic search)
 - Keyword search is looking for the matches of the separate words (lexical search)

```
https://www.youtube.com/watch?v=TQ_ck6Q9gSQ&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=43
https://www.youtube.com/watch?v=CRfg7tAsnUU&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=45
```

** Method 4 : ** User query rewriting

 - query template
 - users can be bad at describing what they want -> use LLM to reformulate the user question for a better structure

** Method 5 : ** Document reranking

 - the most relevant document is not always the best
 - LLM can help at reranking the documents

`https://www.youtube.com/watch?v=H4M55Ptc5cM&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R&index=44`


