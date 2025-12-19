# Quickstart: URL Ingestion Pipeline

**Date**: 2025-12-15
**Feature**: [URL Ingestion and Embedding](spec.md)

This guide provides instructions for setting up and running the backend ingestion pipeline.

## 1. Prerequisites

- Python 3.11+
- `uv` installed (`pip install uv`)
- Access to a Qdrant instance
- A Cohere API key

## 2. Setup

### a. Create Project Directory and Virtual Environment

This project will be self-contained within the `backend/` directory.

```bash
# From the repository root
mkdir backend
cd backend
uv venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

### b. Install Dependencies

Create a `requirements.txt` file with the following content:

```
# requirements.txt
requests
beautifulsoup4
PyMuPDF
cohere
qdrant-client
python-dotenv
```

Install the dependencies using `uv`:

```bash
uv pip install -r requirements.txt
```

### c. Configure Environment Variables

Create a `.env` file in the `backend/` directory to store your credentials. **Do not commit this file to version control.**

```
# .env
COHERE_API_KEY="your_cohere_api_key_here"
QDRANT_URL="your_qdrant_instance_url"
QDRANT_API_KEY="your_qdrant_api_key_here"
```

## 3. Running the Pipeline

The ingestion pipeline will be initiated via a main script. All of the project's logic is contained within `src/main.py`.

### a. Prepare Input URLs

Create a file named `urls.txt` in the `backend/` directory and add one URL per line.

```
# urls.txt
https://example.com/page1
https://example.com/another-page.pdf
```

### b. Execute the Ingestion Script

The main script will read the `.env` file, connect to the services, and process the URLs from `urls.txt`.

```bash
python src/main.py --urls-file urls.txt
```

### c. Expected Outcome

- The script will log its progress to the console.
- Any errors (e.g., failed URL fetches) will be reported.
- Upon completion, the vector database will be populated with the embeddings generated from the content of the provided URLs.
- A summary report will be printed to the console, showing the number of pages processed, chunks created, and vectors stored.
