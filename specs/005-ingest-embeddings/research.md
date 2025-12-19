# Research: URL Ingestion Pipeline

**Date**: 2025-12-15
**Feature**: [URL Ingestion and Embedding](spec.md)

This document records the technical decisions made to resolve ambiguities in the feature specification before implementation.

## 1. Python Libraries for Document Parsing

### Decision
- **HTML Parsing**: Use `requests` for fetching content and `BeautifulSoup4` for parsing HTML and extracting text.
- **PDF Parsing**: Use `PyMuPDF` (`fitz`) for extracting text from PDF documents.

### Rationale
- `requests` is the de-facto standard for making HTTP requests in Python. It is simple, reliable, and well-documented.
- `BeautifulSoup4` is a robust and popular library for web scraping and parsing HTML. It gracefully handles malformed HTML and provides a simple API for navigating the parse tree and extracting content.
- `PyMuPDF` is known for its high performance and accuracy in PDF text extraction compared to other libraries like `pdfplumber` or `PyPDF2`.

### Alternatives Considered
- **`lxml`**: Faster than BeautifulSoup for parsing, but can be less forgiving with broken HTML. BeautifulSoup can use `lxml` as its underlying parser, offering a good compromise.
- **`pdfplumber`**: Another excellent library for PDF processing that also extracts table data, which is not a primary requirement for this feature. `PyMuPDF` is generally faster for pure text extraction.

---

## 2. Text Chunking Strategy

### Decision
- Adopt a `RecursiveCharacterTextSplitter` strategy.
- **Default Chunk Size**: 1000 characters.
- **Default Chunk Overlap**: 200 characters.
- These values will be configurable.

### Rationale
- `RecursiveCharacterTextSplitter` is a common and effective strategy for chunking general text. It tries to split text based on a hierarchy of separators (like `\n\n`, `\n`, ` `, ``) to keep related pieces of text together, which is ideal for creating semantically coherent chunks for embedding.
- A chunk size of 1000 characters with a 200-character overlap is a widely used default that balances context preservation with the input token limits of many embedding models.

### Alternatives Considered
- **Fixed-size chunking**: The simplest method, but can break sentences and separate related concepts.
- **Token-based splitting**: More accurate for aligning with model token limits but requires a specific tokenizer for the embedding model being used. The character-based approach is more model-agnostic.

---

## 3. Deterministic ID Generation

### Decision
- Generate a `SHA-256` hash of each text chunk's content to use as its deterministic ID.

### Rationale
- Using a cryptographic hash of the content ensures that identical chunks will always have the same ID. This is fundamental to achieving idempotency in the data ingestion pipeline, as required by **FR-008**.
- `SHA-256` is a standard, widely available hashing algorithm with an extremely low probability of collision, making it a safe choice for generating unique identifiers.

### Alternatives Considered
- **Hashing the source URL + chunk index**: This is also deterministic but has a key drawback: if the source document is updated and the chunking boundaries shift, all subsequent chunk IDs will change, even if the content of those chunks remains the same. Hashing the content itself makes the ID resilient to such changes.
- **Using UUIDs**: UUIDs are unique but not deterministic. They would not prevent duplicate data from being inserted if the pipeline were to run multiple times on the same source content.
