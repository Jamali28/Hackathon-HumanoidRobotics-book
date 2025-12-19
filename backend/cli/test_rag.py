#!/usr/bin/env python3
"""
Professional CLI-based RAG Testing Tool

A command-line interface for testing the RAG chatbot end-to-end.
"""

import argparse
import json
import logging
import sys
import requests
from typing import Optional
from urllib.parse import urljoin


class RAGTestClient:
    """Client for testing the RAG chatbot API."""

    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({'Content-Type': 'application/json'})

        # Configure logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def test_chat(self, query: str, selected_text: Optional[str] = None,
                  temperature: float = 0.7, max_tokens: int = 1000) -> dict:
        """
        Test the chat endpoint with a query.

        Args:
            query: The main query to send
            selected_text: Optional selected text to include in context
            temperature: Temperature for response generation
            max_tokens: Maximum tokens for the response

        Returns:
            Response dictionary from the API
        """
        # Prepare the query with selected text if provided
        full_query = query
        if selected_text:
            full_query = f"{query} based on the following text: {selected_text}"

        payload = {
            "message": full_query,
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        endpoint = urljoin(f"{self.base_url}/", "api/chat")

        try:
            self.logger.info(f"Sending query to {endpoint}")
            self.logger.info(f"Query: {query}")

            response = self.session.post(
                endpoint,
                json=payload,
                timeout=self.timeout
            )

            if response.status_code == 200:
                result = response.json()
                self.logger.info("[SUCCESS] Query successful")
                return result
            else:
                self.logger.error(f"[ERROR] API returned status code: {response.status_code}")
                self.logger.error(f"Response: {response.text}")
                return {"error": f"API returned {response.status_code}: {response.text}"}

        except requests.exceptions.ConnectionError:
            error_msg = f"[ERROR] Cannot connect to server at {self.base_url}"
            self.logger.error(error_msg)
            return {"error": error_msg}
        except requests.exceptions.Timeout:
            error_msg = f"[ERROR] Request timed out after {self.timeout} seconds"
            self.logger.error(error_msg)
            return {"error": error_msg}
        except requests.exceptions.RequestException as e:
            error_msg = f"[ERROR] Request failed: {str(e)}"
            self.logger.error(error_msg)
            return {"error": error_msg}
        except json.JSONDecodeError:
            error_msg = f"[ERROR] Invalid JSON response: {response.text}"
            self.logger.error(error_msg)
            return {"error": error_msg}

    def display_response(self, result: dict):
        """
        Display the response in a formatted way.

        Args:
            result: Response dictionary from the API
        """
        if "error" in result:
            print(f"\n❌ Error: {result['error']}")
            return

        print(f"\n[ROBOT] Assistant Response:")
        response_text = result.get('response', 'No response received')
        # Remove or replace problematic Unicode characters
        safe_response = response_text.encode('ascii', errors='replace').decode('ascii')
        print(f"   {safe_response}")

        print(f"\n[QUERY] Query:")
        query_text = result.get('query', 'N/A')
        safe_query = query_text.encode('ascii', errors='replace').decode('ascii')
        print(f"   {safe_query}")

        sources = result.get('sources', [])
        if sources:
            print(f"\n[SOURCES] Retrieved Sources ({len(sources)}):")
            for i, source in enumerate(sources, 1):
                url = source.get('source_url', 'Unknown')
                safe_url = url.encode('ascii', errors='replace').decode('ascii')

                text_preview = source.get('text', '')[:100]
                safe_text = text_preview.encode('ascii', errors='replace').decode('ascii')

                print(f"   {i}. URL: {safe_url}")
                print(f"      Score: {source.get('score', 'N/A')}")
                print(f"      Preview: {safe_text}{'...' if len(source.get('text', '')) > 100 else ''}")
        else:
            print(f"\n[SOURCES] Retrieved Sources: None")


def main():
    parser = argparse.ArgumentParser(
        description="Professional CLI-based RAG Testing Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s "What are the key concepts in humanoid robotics?"
  %(prog)s "Explain physical AI" --selected-text "Physical AI combines machine learning with physical systems"
  %(prog)s "How do robots learn?" --base-url http://localhost:8000
  %(prog)s "What is embodied intelligence?" --temperature 0.9 --max-tokens 500
        """
    )

    parser.add_argument(
        "query",
        help="The query to send to the RAG chatbot"
    )

    parser.add_argument(
        "--selected-text",
        help="Optional selected text to include in the query context",
        default=None
    )

    parser.add_argument(
        "--base-url",
        help="Base URL of the RAG API (default: http://localhost:8000)",
        default="http://localhost:8000"
    )

    parser.add_argument(
        "--temperature",
        help="Temperature for response generation (default: 0.7)",
        type=float,
        default=0.7
    )

    parser.add_argument(
        "--max-tokens",
        help="Maximum tokens for response generation (default: 1000)",
        type=int,
        default=1000
    )

    parser.add_argument(
        "--timeout",
        help="Request timeout in seconds (default: 30)",
        type=int,
        default=30
    )

    args = parser.parse_args()

    # Create the test client
    client = RAGTestClient(base_url=args.base_url, timeout=args.timeout)

    # Execute the test
    result = client.test_chat(
        query=args.query,
        selected_text=args.selected_text,
        temperature=args.temperature,
        max_tokens=args.max_tokens
    )

    # Display the formatted response
    client.display_response(result)

    # Exit with appropriate code
    if "error" in result:
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()