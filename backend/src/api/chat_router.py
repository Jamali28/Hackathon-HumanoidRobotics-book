from fastapi import APIRouter, HTTPException
from datetime import datetime
import logging

from src.models.request_response import ChatRequest, ChatResponse
from src.agents.rag_agent import RAGAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Chat endpoint that processes user queries using the RAG agent.
    """
    try:
        logger.info(f"Received chat request: {request.message[:50]}...")

        # Initialize the RAG agent
        agent = RAGAgent()

        # Process the query with the agent
        result = agent.chat(
            query=request.message,
            temperature=request.temperature,
            max_tokens=request.max_tokens
        )

        # Create the response
        response = ChatResponse(
            response=result["response"],
            sources=result["sources"],
            query=result["query"],
            timestamp=result["timestamp"]
        )

        logger.info(f"Successfully processed chat request, response length: {len(result['response'])}")
        return response

    except Exception as e:
        logger.error(f"Error processing chat request: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")

@router.get("/health")
async def chat_health():
    """
    Health check for the chat service.
    """
    return {"status": "chat service healthy", "timestamp": datetime.now().isoformat()}