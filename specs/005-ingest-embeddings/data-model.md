# Data Model: Ingestion Pipeline

**Date**: 2025-12-15
**Feature**: [URL Ingestion and Embedding](spec.md)

This document defines the key data entities for the content ingestion pipeline, based on the feature specification.

## Entity Definitions

### 1. SourceURL

Represents a URL to be ingested.

- **`url`**: `string` (Primary Identifier)
  - The fully qualified URL of the source document.
  - *Validation*: Must be a valid URL format.

### 2. ProcessedDocument

Represents a document that has been fetched, processed, and stored. The ID is used for idempotency checks.

- **`id`**: `string` (Primary Key)
  - A deterministic hash of the `source_url`.
- **`source_url`**: `string`
  - The original URL of the document.
- **`cleaned_text`**: `string`
  - The full text extracted from the document after cleaning.
- **`processed_at`**: `datetime`
  - Timestamp of when the document was last processed.

### 3. TextChunk

Represents a single chunk of text to be embedded. This is the core unit of data for the vector store.

- **`id`**: `string` (Primary Key)
  - A deterministic `SHA-256` hash of the `content`.
- **`document_id`**: `string` (Foreign Key to `ProcessedDocument.id`)
  - The ID of the parent document.
- **`content`**: `string`
  - The text content of the chunk.
- **`chunk_index`**: `integer`
  - The 0-based index of the chunk within the parent document.
- **`metadata`**: `object`
  - A flexible field for storing additional metadata, such as:
    - `source_url`: The original URL.
    - `page_number`: If applicable (for PDFs).

### 4. VectorEmbedding

Represents the stored vector in the vector database (e.g., Qdrant). In practice, this entity is managed by the vector database, and the `TextChunk` `id` is used as the vector's ID.

- **`id`**: `string` (Matches `TextChunk.id`)
- **`vector`**: `array<float>`
  - The dense vector representation of the text chunk content.
- **`payload`**: `object` (Matches `TextChunk` entity)
  - The associated metadata stored alongside the vector.

## Relationships

- A `ProcessedDocument` has a one-to-many relationship with `TextChunk`.
- Each `TextChunk` has a one-to-one relationship with a `VectorEmbedding` in the vector database.
