# Quickstart Guide

This guide provides a high-level overview of how to set up, run, and deploy the Docusaurus textbook and its associated RAG backend.

## Prerequisites

-   Node.js (LTS version)
-   Python 3.11+
-   Docker (for local instances of Qdrant/Postgres, if not using cloud services)
-   An account with Qdrant Cloud, Neon Postgres, and OpenAI.

## Frontend (Docusaurus Textbook)

### 1. Installation

Navigate to the `frontend/` directory (or project root if a single project structure is used) and run:

```bash
npm install
```

### 2. Running Locally

To start the Docusaurus development server:

```bash
npm run start
```

The textbook will be available at `http://localhost:3000`.

### 3. Building for Production

To build the static site for production:

```bash
npm run build
```

The output will be in the `build/` directory.

### 4. Deployment

The project is configured for deployment to GitHub Pages. Pushing to the `main` branch will trigger a GitHub Action to build and deploy the site.

## Backend (FastAPI RAG Service)

### 1. Setup

-   Navigate to the `backend/` directory.
-   Create a virtual environment: `python -m venv venv`
-   Activate the virtual environment: `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
-   Install dependencies: `pip install -r requirements.txt`
-   Set up a `.env` file with your credentials for Qdrant, Neon, and OpenAI.

### 2. Running Locally

To start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

### 3. Data Ingestion
To populate the Qdrant and Neon databases, you will need to run the ingestion scripts:
1.  **Chunking**: Run `python chunking.py` to process the Docusaurus content into chunks.
2.  **Loading**: Run `python qdrant_loader.py` and `python postgres_loader.py` to load the data into their respective databases.

## Full Project Structure

This project follows a `frontend` / `backend` structure.

```text
/
├── backend/
│   ├── src/
│   │   ├── api/
│   │   ├── services/
│   │   └── models/
│   ├── tests/
│   └── requirements.txt
├── frontend/ (Docusaurus root)
│   ├── docs/
│   ├── src/
│   ├── docusaurus.config.js
│   └── package.json
└── specs/
    └── 001-docusaurus-textbook/
        ├── plan.md
        ├── spec.md
        └── ...
```
