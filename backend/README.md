# Backend URL Ingestion and Embedding Pipeline

This project implements a Python-based pipeline to ingest content from specified URLs (HTML and PDF), extract clean text, chunk it, generate Cohere embeddings, and store them in a Qdrant vector database.

## Features

- Fetches URLs from a sitemap.
- Extracts text from HTML and PDF documents.
- Chunks text into smaller, semantically coherent pieces.
- Generates vector embeddings using Cohere's `embed-english-v3.0` model.
- Stores text chunks and their embeddings in Qdrant with deterministic IDs for idempotency.

## Setup

### Prerequisites

- Python 3.11+
- `uv` (ultra-fast Python package installer and resolver) installed. If not, install via `pip install uv`.
- Access to a Qdrant instance (local or cloud).
- A Cohere API key.

### Installation

1.  **Navigate to the `backend/` directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    uv venv
    source .venv/bin/activate  # On macOS/Linux
    # For Windows, use: .venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```

### Configuration

Create a `.env` file in the `backend/` directory based on the provided `.env.example`. This file will store your API keys and Qdrant connection details.

```
# backend/.env
COHERE_API_KEY="your_cohere_api_key_here"
QDRANT_URL="your_qdrant_instance_url"
QDRANT_API_KEY="your_qdrant_api_key_here"
```

**Ensure you do NOT commit your `.env` file to version control.**

## Usage

Run the pipeline from the `backend/` directory, providing the URL to your sitemap.

```bash
python src/main.py --sitemap-url "https://example.com/sitemap.xml"
```

Replace `"https://example.com/sitemap.xml"` with the actual URL of the sitemap you wish to ingest.

### Example

To ingest the provided textbook sitemap:

```bash
python src/main.py --sitemap-url "https://hackathon-humanoid-robotics-book-fk.vercel.app/sitemap.xml"
```

## Logging

The pipeline outputs logs to the console, providing information on the fetching, parsing, chunking, embedding, and storage processes, as well as any errors encountered.

## Error Handling

The pipeline includes robust error handling for network requests, API calls, and content processing to ensure graceful degradation and informative logging in case of issues.
