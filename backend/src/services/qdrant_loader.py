import os
from qdrant_client import QdrantClient, models
from typing import List
from backend.src.models.rag_models import ContentChunk

QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "physical_ai_textbook_chunks"

def initialize_qdrant_client():
    client = QdrantClient(
        host=QDRANT_HOST,
        port=QDRANT_PORT,
        api_key=QDRANT_API_KEY
    )
    return client

def create_collection_if_not_exists(client: QdrantClient, vector_size: int):
    # Check if collection already exists
    collections = client.get_collections().collections
    if COLLECTION_NAME not in [c.name for c in collections]:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=models.VectorParams(size=vector_size, distance=models.Distance.COSINE),
        )
        print(f"Collection '{COLLECTION_NAME}' created with vector size {vector_size}.")
    else:
        print(f"Collection '{COLLECTION_NAME}' already exists.")


def upload_chunks_to_qdrant(client: QdrantClient, chunks: List[ContentChunk]):
    points = []
    for chunk in chunks:
        points.append(
            models.PointStruct(
                id=chunk.chunk_id,
                vector=chunk.vector,
                payload=chunk.metadata.dict() # Store metadata as payload
            )
        )
    
    if points:
        client.upsert(
            collection_name=COLLECTION_NAME,
            wait=True,
            points=points
        )
        print(f"Uploaded {len(points)} chunks to Qdrant collection '{COLLECTION_NAME}'.")
    else:
        print("No chunks to upload to Qdrant.")

if __name__ == "__main__":
    # Example usage:
    # Requires an embedding model to generate actual vectors.
    # For now, we'll use dummy chunks.
    
    # Dummy chunks (replace with actual chunks from chunking.py and an embedding model)
    dummy_chunks = [
        ContentChunk(
            chunk_id="intro-0",
            chapter_id="introduction",
            content="This is the first part of the introduction.",
            vector=[0.1] * 768,
            metadata={
                "source_path": "frontend/docs/introduction.md",
                "title": "Introduction",
                "keywords": ["intro", "course"],
                "headings": ["Introduction"]
            }
        ),
        ContentChunk(
            chunk_id="intro-1",
            chapter_id="introduction",
            content="This is the second part, discussing physical AI concepts.",
            vector=[0.2] * 768,
            metadata={
                "source_path": "frontend/docs/introduction.md",
                "title": "Introduction",
                "keywords": ["physical ai", "concepts"],
                "headings": ["Physical AI Concepts"]
            }
        )
    ]

    client = initialize_qdrant_client()
    create_collection_if_not_exists(client, vector_size=768) # Assuming 768-dim embeddings
    upload_chunks_to_qdrant(client, dummy_chunks)
