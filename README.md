# PDF Chatbot

A RAG (Retrieval-Augmented Generation) chatbot that answers questions based on your own PDF documents, using OpenAI embeddings, ChromaDB as a vector store, and Gradio as the UI.

## How It Works

1. PDFs are loaded and split into chunks
2. Each chunk is embedded using OpenAI's `text-embedding-3-large` model and stored in ChromaDB
3. When a user asks a question, the retriever finds the most relevant chunks
4. The chunks are passed to `gpt-4o-mini` as context, which generates a response

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure environment variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Add PDF documents

Place your PDF files in the `data/` directory.

### 4. Ingest the documents

Run this once to embed your PDFs and populate the vector store:

```bash
python ingest_database.py
```

### 5. Start the chatbot

```bash
python chatbot.py
```

Then open the Gradio URL shown in the terminal (e.g. `http://127.0.0.1:7860`).

## Project Structure

```
├── chatbot.py              # Gradio chatbot app
├── ingest_database.py      # PDF ingestion and embedding pipeline
├── data/                   # Place your PDF files here
├── chroma_db/              # Generated vector store (auto-created)
├── .env                    # Your API keys (not committed to git)
├── requirements.txt
└── README.md
```

## Configuration

| Setting | Location | Default |
|---------|----------|---------|
| Embedding model | both files | `text-embedding-3-large` |
| LLM model | `chatbot.py` | `gpt-4o-mini` |
| LLM temperature | `chatbot.py` | `0.5` |
| Number of retrieved chunks | `chatbot.py` | `5` |
| Chunk size | `ingest_database.py` | `300` |
| Chunk overlap | `ingest_database.py` | `200` |