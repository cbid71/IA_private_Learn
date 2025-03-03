# About improving retrieval by adding metadata

## Reminder

- raw files ( aka `documents` ) can be cut by conceptual ideas -> chunks
- chunks can be cut in words or subwords -> tokens
- tokens can be mathematically transcribed with near value (high cosine similarity) depending of conceptual bounds -> vectors

To improve the retrieval of relevant documents/vectors/others we can add metadata to each of those raw files, chunks, tokens or vectors, and each of those levels have their importance

## How to add metadata to files/documents, chunks, tokens or vectors ?


There are several tools and methods to enrich documents, chunks, or tokens with metadata. Here's a detailed guide to explain how to proceed practically, using popular tools and some best practices. I'll provide solutions suited for different levels of enrichment (document, chunk, token).

### 1. **Enriching Documents (global level)**

To enrich documents with metadata, the goal is to add information like the date, author, topic, or any other relevant data to the document's structure in your database. Here's how you can do it:

#### Method:
- **Manual extraction of metadata**: If your documents are already organized (e.g., articles or reports in a structured format like JSON, XML, or even a database format), you can simply add additional fields for the metadata.

  Example of a JSON structure for an enriched document:
  ```json
  {
      "id": "1234",
      "content": "This is an example of content...",
      "metadata": {
          "author": "John Doe",
          "publication_date": "2025-03-01",
          "topic": "Artificial Intelligence",
          "source": "Scientific article"
      }
  }
  ```

#### Tools:
- **Elasticsearch**: If you're using Elasticsearch to index your documents, you can easily add metadata during indexing by including additional fields. Elasticsearch allows you to structure data and perform highly efficient searches on this metadata.
  - Example of an indexing query in Elasticsearch:
    ```json
    PUT /my_index/_doc/1234
    {
        "content": "This is an example of content...",
        "metadata": {
            "author": "John Doe",
            "publication_date": "2025-03-01",
            "topic": "Artificial Intelligence",
            "source": "Scientific article"
        }
    }
    ```
- **Apache Tika**: If you have documents in various formats (PDF, DOCX, HTML, etc.), **Apache Tika** can be used to automatically extract metadata, such as title, author, creation date, etc.

---

### 2. **Enriching Chunks (text segments)**

When a document is too large, it's often divided into chunks for better management. Enriching chunks means adding metadata that depends on their position or role in the text, such as the type of section (introduction, conclusion, etc.), relevance, or even semantic tags.

#### Method:
- **Splitting the document into chunks**: You can divide your text into smaller pieces, such as paragraphs or sentences, and then add information about each piece, such as its role in the document or the section it represents.

  Example of a JSON structure for an enriched chunk:
  ```json
  {
      "chunk_id": "chunk_001",
      "content": "This is a paragraph in the introduction.",
      "metadata": {
          "section": "Introduction",
          "position_in_doc": "1",
          "context": "General introduction to AI"
      }
  }
  ```

#### Tools:
- **SpaCy**: To split text into chunks and add additional information, you can use **SpaCy** to analyze the text and then break it down into sentences, paragraphs, or entities.
  - **Example**:
    ```python
    import spacy
    nlp = spacy.load("fr_core_news_sm")
    
    text = "This is an example. This is the second sentence."
    doc = nlp(text)
    
    chunks = []
    for sent in doc.sents:
        chunks.append({
            "content": sent.text,
            "metadata": {
                "section": "Introduction",
                "position_in_doc": doc.start_char,
            }
        })
    print(chunks)
    ```

- **Langchain**: If you're using Langchain to build your pipeline, you can add metadata to chunks by using text indexing and transformation tools. For example, Langchain allows you to split text and add contextual metadata to the chunks.

---

### 3. **Enriching Tokens (granular level)**

Enriching **tokens** involves adding very detailed information to each word or subword, such as its grammatical role, position in the text, or named entities it contains.

#### Method:
- **Token annotation**: This involves identifying entities in the text and assigning metadata to them. For example, you can identify place names, people, or key concepts and associate them with metadata.

  Example of a structure for an enriched token:
  ```json
  {
      "token": "Artificial Intelligence",
      "metadata": {
          "type": "named_entity",
          "category": "technology",
          "position_in_chunk": "2"
      }
  }
  ```

#### Tools:
- **SpaCy**: SpaCy is also useful for enriching tokens because it allows you to identify named entities (persons, places, organizations) and annotate each token with grammatical information.
  - Example of annotation with SpaCy:
    ```python
    import spacy
    nlp = spacy.load("fr_core_news_sm")
    
    text = "Artificial intelligence is an exciting field."
    doc = nlp(text)
    
    tokens_with_metadata = []
    for token in doc:
        tokens_with_metadata.append({
            "token": token.text,
            "metadata": {
                "lemma": token.lemma_,
                "pos": token.pos_,
                "is_stop": token.is_stop,
                "ent_type": token.ent_type_
            }
        })
    print(tokens_with_metadata)
    ```

- **Hugging Face Tokenizers**: If you're using language models like BERT or GPT, you can use the **Hugging Face Tokenizers** library to split text into tokens and add metadata to each one.

---

### Summary:
To enrich your documents, chunks, or tokens, you can:
- Use **Elasticsearch** to add metadata globally to a document.
- Use libraries like **SpaCy** to split the text into chunks and add metadata at the section level.
- For token-level enrichment, **SpaCy** is also a great choice as it allows annotating each word with detailed information about its nature (named entity, grammatical role, etc.).
