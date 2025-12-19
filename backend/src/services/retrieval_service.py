import os
import logging
from typing import List, Dict, Optional
from dotenv import load_dotenv
import cohere
from qdrant_client import QdrantClient
from qdrant_client.http.models import models
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class RetrievalService:
    def __init__(self):
        self.cohere_api_key = os.getenv("COHERE_API_KEY")
        self.qdrant_url = os.getenv("QDRANT_URL")
        self.qdrant_api_key = os.getenv("QDRANT_API_KEY")

        if not all([self.cohere_api_key, self.qdrant_url, self.qdrant_api_key]):
            raise ValueError("Missing required environment variables: COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY")

        self.co = cohere.Client(self.cohere_api_key)
        self.client = QdrantClient(url=self.qdrant_url, api_key=self.qdrant_api_key)
        self.collection_name = "rag_embedding"

        logger.info("Retrieval Service initialized successfully.")

    def generate_query_embedding(self, query: str) -> List[float]:
        """
        Generate embeddings for a query using the same Cohere model as ingestion.

        Args:
            query: The query text to embed

        Returns:
            A list of floats representing the embedding vector
        """
        try:
            response = self.co.embed(
                texts=[query],
                model='embed-english-v3.0',  # Same model used during ingestion
                input_type='search_query'     # Specify this is a search query
            )
            embedding = response.embeddings[0]
            logger.info(f"Generated embedding for query (length: {len(query)}).")
            return embedding
        except Exception as e:
            logger.error(f"Error generating query embedding: {e}")
            raise

    def retrieve_chunks(self, query: str, top_k: int = 5, score_threshold: float = 0.3) -> List[Dict]:
        """
        Retrieve relevant chunks from Qdrant based on the query embedding.

        Args:
            query: The query text
            top_k: Number of top results to retrieve
            score_threshold: Minimum similarity score threshold

        Returns:
            List of dictionaries containing retrieved chunks with metadata
        """
        query_embedding = self.generate_query_embedding(query)

        try:
            # Perform semantic search in Qdrant
            search_results = self.client.query_points(
                collection_name=self.collection_name,
                query=query_embedding,
                limit=top_k,
                with_payload=True,
                with_vectors=False,
                score_threshold=score_threshold
            ).points

            retrieved_chunks = []
            for result in search_results:
                chunk_data = {
                    'id': result.id,
                    'score': result.score,
                    'text': result.payload.get('text', ''),
                    'source_url': result.payload.get('source_url', 'Unknown'),
                    'chunk_index': result.payload.get('chunk_index', -1),
                    'metadata': result.payload
                }
                retrieved_chunks.append(chunk_data)

            logger.info(f"Retrieved {len(retrieved_chunks)} chunks for query: '{query[:50]}...'")
            return retrieved_chunks

        except Exception as e:
            logger.error(f"Error retrieving chunks from Qdrant: {e}")
            raise

    def retrieve_context(self, query: str, top_k: int = 5) -> str:
        """
        Retrieve context as a formatted string for the agent.

        Args:
            query: The query text
            top_k: Number of top results to retrieve

        Returns:
            Formatted context string containing relevant chunks
        """
        chunks = self.retrieve_chunks(query, top_k)

        if not chunks:
            return "No relevant context found in the knowledge base."

        context_parts = []
        for i, chunk in enumerate(chunks):
            context_parts.append(
                f"Context Chunk {i+1} (Score: {chunk['score']:.3f}, Source: {chunk['source_url']}):\n"
                f"{chunk['text']}\n"
            )

        return "\n".join(context_parts)