# Physical AI & Humanoid Robotics Textbook

This repository contains the source code for the Docusaurus-based textbook on Physical AI & Humanoid Robotics, along with a RAG chatbot backend.

## Deployment

The Docusaurus textbook is designed to be deployed to GitHub Pages.

### Frontend (Docusaurus) Deployment

1.  Ensure your repository is configured for GitHub Pages (e.g., `gh-pages` branch deployment).
2.  Push changes to the `main` branch. A GitHub Actions workflow (`.github/workflows/deploy.yml`) will automatically build and deploy the Docusaurus site.
3.  Alternatively, you can manually trigger the workflow from the GitHub Actions tab.

### Backend (FastAPI RAG Service) Deployment

Deployment of the FastAPI backend will require a separate hosting environment (e.g., a cloud VM, serverless function).
1.  Ensure you have your environment variables set for `OPENAI_API_KEY`, `QDRANT_HOST`, `QDRANT_PORT`, `QDRANT_API_KEY`, and `NEON_PG_CONN_STRING`.
2.  Run the ingestion scripts (`chunking.py`, `qdrant_loader.py`, `postgres_loader.py`) to populate your Qdrant and Neon Postgres instances.
3.  Deploy the FastAPI application using a production-ready ASGI server like Gunicorn or Uvicorn.
    Example: `gunicorn -w 4 -k uvicorn.workers.UvicornWorker backend.src.api.main:app`
