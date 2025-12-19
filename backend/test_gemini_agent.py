import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set a fake GEMINI_API_KEY for testing purposes
os.environ['GEMINI_API_KEY'] = 'fake-key-for-testing'
os.environ['COHERE_API_KEY'] = 'fake-key-for-testing'
os.environ['QDRANT_URL'] = 'fake-url-for-testing'
os.environ['QDRANT_API_KEY'] = 'fake-key-for-testing'

try:
    from src.agents.rag_agent import RAGAgent
    print("Attempting to create RAGAgent instance...")

    # This should fail with API key validation but not with OPENAI_API_KEY error
    agent = RAGAgent()
    print("RAGAgent created successfully (using Gemini configuration)")

except ValueError as e:
    if "OPENAI_API_KEY" in str(e):
        print(f"ERROR: Still using OpenAI configuration: {e}")
    elif "GEMINI_API_KEY" in str(e):
        print(f"Expected error with Gemini configuration: {e}")
        print("This is expected if we don't have a real API key")
    else:
        print(f"Different error: {e}")

except Exception as e:
    print(f"Other error: {e}")
    # This might happen if there are issues with Qdrant connection, etc.
    if "OPENAI_API_KEY" in str(e):
        print("ERROR: Still referencing OpenAI in the code somewhere!")