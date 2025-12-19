import traceback
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set fake keys for testing
os.environ['GEMINI_API_KEY'] = 'fake-key'
os.environ['COHERE_API_KEY'] = 'fake-key'
os.environ['QDRANT_URL'] = 'fake-url'
os.environ['QDRANT_API_KEY'] = 'fake-key'

try:
    # Import the modules exactly as the API would
    from src.agents.rag_agent import RAGAgent
    print("Successfully imported RAGAgent")

    # Try to instantiate the agent
    agent = RAGAgent()
    print("Successfully instantiated RAGAgent with Gemini configuration")

    # Try to call the chat method to see where the error occurs
    result = agent.chat("test query")
    print("Chat method executed without OPENAI_API_KEY error")

except Exception as e:
    print(f"Error occurred: {e}")
    print("Full traceback:")
    traceback.print_exc()