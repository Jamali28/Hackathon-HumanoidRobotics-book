import json
from typing import Dict, Any
from src.services.retrieval_service import RetrievalService

class RetrievalTool:
    """
    A tool for the OpenAI agent to retrieve relevant context from the vector database.
    """

    def __init__(self):
        self.retrieval_service = RetrievalService()

    @property
    def tool_definition(self):
        """
        Returns the tool definition for OpenAI's function calling.
        """
        return {
            "type": "function",
            "function": {
                "name": "retrieve_context",
                "description": "Retrieve relevant context from the humanoid robotics knowledge base",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The search query to find relevant context"
                        },
                        "top_k": {
                            "type": "integer",
                            "description": "Number of top results to retrieve (default: 5)",
                            "default": 5
                        }
                    },
                    "required": ["query"]
                }
            }
        }

    def retrieve_context(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        """
        Retrieve context from the vector database based on the query.

        Args:
            query: The search query
            top_k: Number of top results to retrieve

        Returns:
            Dictionary containing the retrieved context and metadata
        """
        try:
            chunks = self.retrieval_service.retrieve_chunks(query, top_k)

            # Format the results for the agent
            formatted_chunks = []
            sources = []

            for chunk in chunks:
                formatted_chunks.append({
                    "id": chunk['id'],
                    "text": chunk['text'][:500] + "..." if len(chunk['text']) > 500 else chunk['text'],  # Truncate long texts
                    "score": chunk['score'],
                    "source_url": chunk['source_url']
                })
                sources.append({
                    "id": chunk['id'],
                    "source_url": chunk['source_url'],
                    "score": chunk['score']
                })

            return {
                "context": self.retrieval_service.retrieve_context(query, top_k),
                "chunks": formatted_chunks,
                "sources": sources,
                "query": query,
                "retrieved_count": len(chunks)
            }
        except Exception as e:
            return {
                "error": f"Error retrieving context: {str(e)}",
                "context": "No context available due to retrieval error.",
                "chunks": [],
                "sources": [],
                "query": query,
                "retrieved_count": 0
            }

    def call(self, tool_input: Dict[str, Any]) -> str:
        """
        Call the retrieval tool with the given input.

        Args:
            tool_input: Dictionary containing the tool parameters

        Returns:
            JSON string of the retrieval results
        """
        query = tool_input.get("query")
        top_k = tool_input.get("top_k", 5)

        results = self.retrieve_context(query, top_k)
        return json.dumps(results, indent=2)