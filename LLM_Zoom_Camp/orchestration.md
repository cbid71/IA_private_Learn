# Orchestration

https://github.com/DataTalksClub/llm-zoomcamp/tree/main/05-orchestration

We work through pipelines of data submitted to models

Data path :

Load -> Transform -> Export -> Index

 - Load = raw data or inference
 - Transform = cut in pieces of texts (chunks)
 - Export = storing results, embed dings/vectors
 - Index = 

## Ingest



## Chunk, tokenization, and the difference between the two

Chunk : segmenting larger text into coherent units to aid in retrieval and context
Tokenization : Process of breaking down text into individual tokens (words or subwirds) for fu>


| **Aspect**           | **Chunking**                                | **Tokenization**                              |
|----------------------|---------------------------------------------|-----------------------------------------------|
| **Purpose**          | Groups tokens into larger, meaningful units (chunks). | Breaks text into smaller units (tokens).      |
| **Output**           | Phrases or groups of tokens (e.g., noun phrases, verb phrases). | Individual tokens (e.g., words, subwords).    |
| **Example Text**     | "The quick brown fox jumps."               | "The quick brown fox jumps."                 |
| **Example Tokens**   | [NP: "The quick brown fox", VP: "jumps"]   | ["The", "quick", "brown", "fox", "jumps"]     |
| **Process**          | Grouping related tokens into phrases.      | Splitting text into basic units.              |
| **Usage**            | Helps in understanding sentence structure. | First step in NLP tasks like text analysis.   |


## Embed

Embedding : The process of converting tokens into vectors capturing the semantic meaning 

Note : It can be vectors, but their are also numerous other ways to store data (graph knowledge capturing the relationship between entities and concepts in the data)

## Export

Note : learn elasticsearch :3

## Orchestration/Trigger

Strongly depends of your architecture, it could be lambda+eventbridge, shedulers, events etc... to ingest data and get a result.

