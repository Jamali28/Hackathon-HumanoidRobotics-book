# Data Model

This document outlines the data models for the entities involved in the RAG (Retrieval Augmented Generation) system. The primary focus is on how content is structured, stored, and retrieved.

## Core Entities

### 1. `ContentChunk`

This is the fundamental unit of information for the RAG system. A `Chapter` from the Docusaurus site will be broken down into one or more `ContentChunk` entities.

-   **`chunk_id`**: `string` (Primary Key, e.g., a UUID) - A unique identifier for the chunk.
-   **`chapter_id`**: `string` - The unique ID of the source chapter (from Docusaurus frontmatter).
-   **`content`**: `text` - The actual text content of the chunk.
-   **`vector`**: `array[float]` - The vector embedding of the `content`, to be stored in Qdrant.
-   **`metadata`**: `object` - A JSON object containing additional context. See `Metadata` entity below.

### 2. `Metadata`

This entity contains all the contextual information associated with a `ContentChunk`. It is crucial for filtering and providing source information in RAG responses.

-   **`source_path`**: `string` - The file path to the original Markdown file (e.g., `docs/modules/module1-ros2.md`).
-   **`title`**: `string` - The title of the chapter.
-   **`module`**: `string` (optional) - The name of the module the chapter belongs to.
-   **`week`**: `integer` (optional) - The week number the chapter belongs to.
-   **`keywords`**: `array[string]` - A list of keywords from the chapter's frontmatter.
-   **`headings`**: `array[string]` - A list of headings and subheadings within the chunk's scope, to provide more context.

## Relationships

-   A `Chapter` (from Docusaurus) **has many** `ContentChunk` entities.
-   Each `ContentChunk` **has one** `Metadata` object associated with it.

## Storage Mapping

-   **`ContentChunk.vector`** and **`ContentChunk.chunk_id`** will be stored in **Qdrant Cloud**.
-   **`ContentChunk.metadata`** and the rest of the `ContentChunk` fields will be stored in **Neon Postgres**. The `chunk_id` will be used as a foreign key to link the Qdrant vector to the Postgres metadata record.
