# Implementation Plan: URL Ingestion and Embedding Pipeline

**Branch**: `005-ingest-embeddings` | **Date**: 2025-12-15 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/005-ingest-embeddings/spec.md`

## Summary

This plan outlines the technical design for a backend data ingestion pipeline. The system will fetch content from a list of URLs (HTML and PDF), extract clean text, generate vector embeddings using Cohere, and store them idempotently in a Qdrant vector database. The project will be implemented in Python using `uv` for dependency management.

## Technical Context

**Language/Version**: Python 3.11
**Primary Dependencies**: `uv`, `requests`, `beautifulsoup4`, `PyMuPDF`, `cohere`, `qdrant-client`
**Storage**: Qdrant (Vector Database)
**Testing**: `pytest`
**Target Platform**: Backend script running in a server environment (e.g., Linux).
**Project Type**: Backend service (contained in the `backend/` directory).
**Performance Goals**: N/A for initial implementation; focus is on correctness and idempotency.
**Constraints**: Must be able to handle both HTML and PDF documents. The process must not create duplicate entries on re-runs.
**Scale/Scope**: Designed to process a list of URLs provided in a file.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **Accuracy**: The plan ensures content is directly fetched from user-provided source URLs.
- [X] **Clarity**: The proposed solution is a standard backend pipeline, understandable to engineers.
- [X] **Reproducibility**: The pipeline is designed to be deterministic and repeatable. `uv` ensures reproducible environments.
- [X] **Consistency**: The plan establishes a clear structure for the backend service.
- [X] **Source-Grounded Reasoning**: The pipeline is grounded entirely on the content from the source URLs.
- [X] **Docusaurus-Compatibility**: Not applicable to this backend feature.
- [X] **Static Deployment**: Not applicable to this backend feature.
- [X] **PowerShell Compatibility**: The project itself is Python-based. `uv` and Python commands are cross-platform.

## Project Structure
## urls  
Target site : https://hackathon-humanoid-robotics-book-fk.vercel.app/
sitemap URL : https://hackathon-humanoid-robotics-book-fk.vercel.app/sitemap.xml




### Documentation (this feature)

```text
specs/005-ingest-embeddings/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
└── contracts/           # Not generated for this feature
```

### Source Code (repository root)

```text
backend/
├── src/
│   └── main.py          # All logic for fetching, parsing, embedding, storing
├── .env                 # Environment variables
├── requirements.txt     # Project dependencies
└── urls.txt             # Input file with URLs to process
```

### Internal File Structure (`backend/src/main.py`)

The `main.py` file will be structured with the following key functions to implement the pipeline logic:

- **`get_all_urls(url: str) -> List[str]`**: Crawls the initial URL to find all relevant sub-pages to ingest. For the initial version, this might just read from a `urls.txt` file.
- **`extract_text_from_url(url: str) -> str`**: Fetches content from a single URL and, based on its type (HTML/PDF), uses the appropriate parser (`BeautifulSoup` or `PyMuPDF`) to extract clean text.
- **`chunk_text(text: str) -> List[str]`**: Takes a long text and splits it into smaller, deterministic chunks using the `RecursiveCharacterTextSplitter` strategy.
- **`embed(chunks: List[str]) -> List[List[float]]`**: Takes a list of text chunks and uses the Cohere client to generate a vector embedding for each one.
- **`create_collection(collection_name: str)`**: Ensures a collection named `rag_embedding` exists in Qdrant with the correct vector parameters.
- **`save_chunk_to_qdrant(chunk: str, embedding: List[float])`**: Saves a single text chunk and its corresponding embedding to the Qdrant collection. It will use a deterministic ID (SHA256 hash of the content) for idempotency.
- **`main()`**: The main execution function that orchestrates the entire pipeline:
    1. Calls `get_all_urls`.
    2. Calls `create_collection`.
    3. Iterates through each URL, calling `extract_text_from_url`, `chunk_text`, `embed`, and `save_chunk_to_qdrant` for each piece of content.


**Structure Decision**: Per the user's request, the implementation will be consolidated into a single file (`src/main.py`). This approach is suitable for a linear, script-based pipeline and simplifies the project structure for this initial version.

## Complexity Tracking

No violations of the constitution were necessary.