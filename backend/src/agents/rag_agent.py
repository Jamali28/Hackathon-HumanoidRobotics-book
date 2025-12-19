import os
import logging
import json
from typing import Dict, Any, List
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

from src.agents.retrieval_tool import RetrievalTool
from src.models.request_response import SourceChunk

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class RAGAgent:
    """
    A RAG-enabled agent using Google Gemini with custom retrieval tools.
    """

    def __init__(self):
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not self.gemini_api_key:
            # Don't raise an error immediately, just store that we don't have a key
            self.model = None
            logger.warning("GEMINI_API_KEY not set. Agent will return a helpful message when queried.")
        else:
            try:
                # Configure the Gemini API
                genai.configure(api_key=self.gemini_api_key)

                # Initialize the model - using a model that's generally available
                # Use the full model path format for Google Generative Language API
                self.model = genai.GenerativeModel(
                    model_name="models/gemini-1.0-pro",  # Full path format for GLM API
                    generation_config={
                        "temperature": 0.7,
                        "max_output_tokens": 1000,
                    }
                )
            except Exception as e:
                logger.error(f"Error configuring Gemini API: {e}")
                self.model = None
                # Don't raise an exception that stops initialization, just log the error
                logger.warning("Gemini API configuration failed. Agent will respond with configuration error when queried.")

        self.retrieval_tool = RetrievalTool()
        self.system_prompt = """
        You are an expert librarian and subject matter expert for the 'Physical AI & Humanoid Robotics' book. Your role is to answer questions specifically about the content in this book, focusing on humanoid robotics, physical AI, and embodied intelligence.

        When responding to user queries:
        1. Use ONLY the context provided through the retrieval tool from the book
        2. Be factual and precise, citing the specific sources when possible
        3. If the context doesn't contain the answer, clearly state that the information is not available in the book
        4. Keep responses concise but informative, focusing on the book's content
        5. Structure your response with clear explanations based on the book's material
        6. When citing sources, mention the source URL and relevance score if available
        7. Remember that you are a specialist for THIS specific book, not a general AI assistant
        8. If asked about topics outside the book's scope, politely mention that your knowledge is limited to the book content
        """

        logger.info("RAG Agent initialized successfully with Google Gemini.")

    def chat(self, query: str, temperature: float = 0.7, max_tokens: int = 1000) -> Dict[str, Any]:
        """
        Process a chat query using the RAG agent with Google Gemini.

        Args:
            query: The user's query
            temperature: Temperature for response generation
            max_tokens: Maximum tokens for the response

        Returns:
            Dictionary containing the response and sources
        """
        try:
            # Check if we have a configured model
            if self.model is None:
                return {
                    "response": "The AI assistant is not properly configured. Please set the GEMINI_API_KEY environment variable with a valid Google API key.",
                    "sources": [],
                    "query": query,
                    "timestamp": datetime.now().isoformat()
                }

            # Retrieve relevant context using the retrieval tool
            retrieval_result = self.retrieval_tool.retrieve_context(query, top_k=5)
            context = retrieval_result.get("context", "")

            # Prepare the full prompt with context
            full_prompt = f"""
            {self.system_prompt}

            Retrieved Context:
            {context}

            User Query: {query}

            Please provide a helpful response based on the context, citing sources when possible.
            """

            # Configure generation settings
            generation_config = {
                "temperature": temperature,
                "max_output_tokens": max_tokens,
            }

            # Generate content using Gemini
            response = self.model.generate_content(
                full_prompt,
                generation_config=generation_config
            )

            # Extract the text response
            agent_response = response.text if response.text else "I couldn't generate a response. Please try again."

            # Format the sources from the retrieval result
            sources = []
            for chunk in retrieval_result.get("chunks", []):
                sources.append(SourceChunk(
                    id=chunk["id"],
                    text=chunk["text"][:200] + "..." if len(chunk["text"]) > 200 else chunk["text"],
                    score=chunk["score"],
                    source_url=chunk.get("source_url", "Unknown")
                ))

            return {
                "response": agent_response,
                "sources": sources,
                "query": query,
                "timestamp": datetime.now().isoformat()
            }

        except Exception as e:
            logger.error(f"Error in RAG agent chat: {e}")
            # If it's an API-related error, provide a more specific message
            error_msg = str(e)
            if "API_KEY" in error_msg.upper() or "PERMISSION" in error_msg.upper() or "403" in error_msg:
                return {
                    "response": "The AI service is not properly configured. Please check that the GEMINI_API_KEY is set correctly and has the necessary permissions.",
                    "sources": [],
                    "query": query,
                    "timestamp": datetime.now().isoformat()
                }
            elif "404" in error_msg and ("model" in error_msg.lower() or "models/" in error_msg):
                # Handle model not found error - create a response based on retrieved context
                try:
                    # Check if this is a greeting or simple query
                    query_lower = query.lower().strip()
                    if query_lower in ["hi", "hello", "hey", "greetings", "help", "start"]:
                        # For greetings, provide a friendly response with guidance
                        greeting_response = (
                            "Hello! I'm your Physical AI & Humanoid Robotics book assistant. "
                            "I can help you find information about humanoid robotics, physical AI, "
                            "and embodied intelligence from the book content. "
                            "What would you like to know about the book?"
                        )
                        return {
                            "response": greeting_response,
                            "sources": [],
                            "query": query,
                            "timestamp": datetime.now().isoformat()
                        }

                    # For other queries, try to retrieve context
                    retrieval_result = self.retrieval_tool.retrieve_context(query, top_k=5)
                    context_chunks = retrieval_result.get("chunks", [])

                    if context_chunks:
                        # Create a helpful response based on the retrieved context
                        response_text = (f"I found {len(context_chunks)} relevant sections in the book about '{query}'. "
                                       f"Here's what I can tell you based on the available information:\n\n")

                        for i, chunk in enumerate(context_chunks[:3]):  # Show top 3 chunks
                            preview = chunk["text"][:200] + "..." if len(chunk["text"]) > 200 else chunk["text"]
                            response_text += f"{i+1}. {preview}\n\n"

                        response_text += ("\nFor more detailed information, please refer to the sources listed below, "
                                        "or ensure that your GEMINI_API_KEY is configured properly to get AI-generated responses.")

                        sources = []
                        for chunk in context_chunks:
                            sources.append(SourceChunk(
                                id=chunk["id"],
                                text=chunk["text"][:200] + "..." if len(chunk["text"]) > 200 else chunk["text"],
                                score=chunk["score"],
                                source_url=chunk.get("source_url", "Unknown")
                            ))

                        return {
                            "response": response_text,
                            "sources": sources,
                            "query": query,
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "response": f"I couldn't find relevant information about '{query}' in the book content. The AI service is experiencing issues, but I've checked our database and found no matching content. You can ask me about humanoid robotics, physical AI, or embodied intelligence concepts from the book.",
                            "sources": [],
                            "query": query,
                            "timestamp": datetime.now().isoformat()
                        }
                except Exception as fallback_error:
                    logger.error(f"Fallback response generation failed: {fallback_error}")
                    return {
                        "response": f"Sorry, I encountered an error processing your request: {str(e)}. The AI service is currently unavailable due to model configuration issues.",
                        "sources": [],
                        "query": query,
                        "timestamp": datetime.now().isoformat()
                    }
            else:
                return {
                    "response": f"Sorry, I encountered an error processing your request: {str(e)}",
                    "sources": [],
                    "query": query,
                    "timestamp": datetime.now().isoformat()
                }