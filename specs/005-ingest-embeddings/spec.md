# Feature Specification: URL Ingestion and Embedding

**Feature Branch**: `005-ingest-embeddings`  
**Created**: 2025-12-15
**Status**: Draft  
**Input**: User description: "Spec1: URL Ingestion → Embeddings → Vector Store **Title:** Spec1 — Crawl book URLs, generate Cohere embeddings, store in Qdrant **Target audience:** Backend engineers building the RAG ingestion pipeline. **Focus:** Fetch published book pages, extract clean text, chunk content, generate Cohere embeddings, and upsert vectors with metadata into Qdrant Cloud. ## Success criteria - All provided URLs are fetched and processed (errors logged per-URL). - Text is chunked deterministically and embedded using Cohere. - Vectors and metadata are successfully stored in a Qdrant collection. - Re-running the pipeline does **not** create duplicate vectors (idempotent upserts). - Basic kNN search returns relevant chunks for test queries. - Logs report pages processed, chunks created, vectors stored, and failures."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Ingest Content from URLs (Priority: P1)

As a backend engineer, I want to run a pipeline that takes a list of URLs, fetches the content from each URL, and stores it for further processing, so that we can build a knowledge base from published book pages.

**Why this priority**: This is the foundational step for the entire RAG pipeline. Without content, no embeddings can be generated.

**Independent Test**: The pipeline can be run with a set of test URLs, and the raw content of those pages is successfully retrieved and stored in a temporary location.

**Acceptance Scenarios**:

1. **Given** a list of valid URLs, **When** the ingestion pipeline is run, **Then** the HTML content of each URL is successfully downloaded.
2. **Given** a list of URLs containing some invalid or unreachable ones, **When** the ingestion pipeline is run, **Then** the system logs errors for the failed URLs and continues to process the valid ones.

---

### User Story 2 - Process and Chunk Content (Priority: P2)

As a backend engineer, I want the ingestion pipeline to automatically extract clean text from the fetched HTML content and break it into smaller, meaningful chunks, so that it can be effectively used for generating embeddings.

**Why this priority**: Raw HTML is noisy. Clean, well-sized text chunks are essential for generating high-quality embeddings.

**Independent Test**: Provide a sample HTML file to the processing part of the pipeline, and verify that clean text is extracted and divided into chunks according to the defined strategy.

**Acceptance Scenarios**:

1. **Given** fetched HTML content, **When** the processing step is run, **Then** the main textual content is extracted, and boilerplate (like navbars, footers) is removed.
2. **Given** extracted clean text, **When** the chunking step is run, **Then** the text is divided into multiple smaller text chunks of a configured size.

---

### User Story 3 - Generate and Store Embeddings (Priority: P3)

As a backend engineer, I want the pipeline to take the text chunks, generate vector embeddings for them using a configurable embedding service, and store them in a vector database, so that they can be used for semantic search.

**Why this priority**: This step makes the content searchable and "intelligent" by converting text into a machine-understandable format.

**Independent Test**: A set of sample text chunks can be passed to the embedding and storage module, which should generate vectors and correctly store them in the vector database.

**Acceptance Scenarios**:

1. **Given** a set of text chunks, **When** the embedding step is run, **Then** a vector embedding is generated for each chunk.
2. **Given** a set of vector embeddings and their associated metadata, **When** the storage step is run, **Then** they are all successfully saved into the vector database.
3. **Given** that the pipeline is run twice with the same source content, **When** the storage step is complete, **Then** no duplicate entries exist in the vector database.

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST accept a list of URLs as input for the ingestion pipeline.
- **FR-002**: The system MUST fetch the HTML content from each provided URL.
- **FR-003**: The system MUST log an error for any URL that fails to be fetched, and continue processing the remaining URLs.
- **FR-004**: The system MUST extract the main textual content from the fetched HTML, cleaning out irrelevant elements like navigation, ads, and footers.
- **FR-005**: The system MUST divide the cleaned text into deterministic chunks of a configurable size.
- **FR-006**: The system MUST generate a vector embedding for each text chunk using a configured third-party embedding service.
- **FR-007**: The system MUST store each vector embedding along with its corresponding text chunk and metadata (e.g., source URL, chunk ID) in a vector database.
- **FR-008**: The storage process MUST be idempotent. If the pipeline is re-run with the same URLs, duplicate vectors and documents MUST NOT be created.
- **FR-009**: The system MUST log the number of pages processed, chunks created, and vectors stored.

### Key Entities *(include if feature involves data)*

- **URL**: The web address of a source document.
- **Document**: The raw content fetched from a URL.
- **Text Chunk**: A portion of the cleaned text from a document.
- **Embedding**: A vector representation of a text chunk.
- **Vector Metadata**: Data associated with an embedding, such as its source URL and chunk identifier.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of provided URLs are attempted for processing.
- **SC-002**: The pipeline can be re-run on the same data without creating duplicate entries in the vector database.
- **SC-003**: A basic k-Nearest Neighbor (kNN) search on the vector database for a sample query returns relevant text chunks.
- **SC-004**: Pipeline execution logs clearly report the number of pages successfully processed, chunks created, vectors stored, and any failures that occurred.