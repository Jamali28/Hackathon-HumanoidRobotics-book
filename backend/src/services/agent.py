import os
from typing import List, Dict
from qdrant_client import QdrantClient
from openai import OpenAI
from backend.src.models.rag_models import ContentChunk, Metadata
from backend.src.services.qdrant_loader import initialize_qdrant_client, COLLECTION_NAME

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class RAGAgent:
    def __init__(self):
        self.qdrant_client = initialize_qdrant_client()
        self.openai_client = OpenAI(api_key=OPENAI_API_KEY)
        self.embedding_model = "text-embedding-ada-002" # or a more advanced model
        self.llm_model = "gpt-3.5-turbo" # or a more advanced model

    def generate_embedding(self, text: str) -> List[float]:
        """Generates an embedding for the given text using OpenAI."""
        response = self.openai_client.embeddings.create(
            input=text,
            model=self.embedding_model
        )
        return response.data[0].embedding

    def retrieve_chunks(self, query_embedding: List[float], top_k: int = 5) -> List[ContentChunk]:
        """Retrieves relevant chunks from Qdrant based on the query embedding."""
        search_result = self.qdrant_client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_embedding,
            limit=top_k,
            with_payload=True # Retrieve metadata
        )
        
        chunks = []
        for hit in search_result:
            # Need to fetch full content from Postgres based on chunk_id from payload
            # For now, reconstruct based on available info
            metadata = Metadata(**hit.payload)
            # Placeholder for content retrieval from Postgres
            content = f"Content for chunk_id {hit.id} (fetched from Postgres in real impl)"
            chunks.append(ContentChunk(
                chunk_id=hit.id,
                chapter_id=metadata.chapter_id, # Assuming chapter_id is in metadata for now
                content=content,
                vector=hit.vector, # Qdrant returns vector
                metadata=metadata
            ))
        return chunks

    def generate_response(self, query: str, retrieved_chunks: List[ContentChunk]) -> str:
        """Generates a response using the LLM based on the query and retrieved chunks."""
        context = "\n".join([chunk.content for chunk in retrieved_chunks])
        
        messages = [
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
        ]
        
        response = self.openai_client.chat.completions.create(
            model=self.llm_model,
            messages=messages
        )
        return response.choices[0].message.content

    def query(self, user_query: str) -> Dict[str, any]:
        """End-to-end RAG query."""
        query_embedding = self.generate_embedding(user_query)
        retrieved_chunks = self.retrieve_chunks(query_embedding)
        answer = self.generate_response(user_query, retrieved_chunks)

        # Prepare sources for response
        sources = []
        for chunk in retrieved_chunks:
            # Placeholder for actual content and metadata from Postgres
            sources.append({
                "chunk_id": chunk.chunk_id,
                "content": chunk.content,
                "metadata": chunk.metadata.dict()
            })
            
        return {"answer": answer, "sources": sources}

if __name__ == "__main__":
    # Example usage
    agent = RAGAgent()
    user_question = "What are the key components of ROS 2 in humanoid robotics?"
    result = agent.query(user_question)
    print("Answer:", result["answer"])
    print("Sources:", result["sources"])
