import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def start_server():
    """Start the RAG Agent API server."""
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")

    print(f"Starting RAG Agent API server on {host}:{port}")
    print("Press Ctrl+C to stop the server")

    uvicorn.run(
        "src.main:app",
        host=host,
        port=port,
        reload=False,  # Set to True for development
        log_level="info"
    )

if __name__ == "__main__":
    start_server()