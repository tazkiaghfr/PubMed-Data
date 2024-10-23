# PubMed-Data

a LLM system to retrieve medical topic data from PubMed publications and to find answers from those publications

### LLM (Large Language Model)

- **Model:** GPT-3.5-turbo  
- **Description:** Generate answers based on user questions and the context of medical articles retrieved from PubMed.

### RAG (Retrieval-Augmented Generation)

- **Approach:** Data retrieval from PubMed using the Entrez API to gather relevant articles based on user queries.  
- **Description:** Combine language modeling (LLM) with information retrieval, where the retrieved data (articles) serves as context to answer the questions

### Entrez API

- **Methods:**
  - **esearch:** Searches for articles based on the user query and returns article IDs.
  - **efetch:** Retrieves the text of the article (abstract) based on the IDs obtained from the search.
