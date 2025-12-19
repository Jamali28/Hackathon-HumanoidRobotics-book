import requests
import json

# Test the API endpoints
BASE_URL = "http://localhost:8001"

def test_health_endpoint():
    """Test the health endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Health endpoint: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Health endpoint error: {e}")

def test_root_endpoint():
    """Test the root endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Root endpoint: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Root endpoint error: {e}")

def test_chat_endpoint():
    """Test the chat endpoint"""
    try:
        payload = {
            "message": "What are the key concepts in humanoid robotics?",
            "temperature": 0.7,
            "max_tokens": 500
        }
        response = requests.post(f"{BASE_URL}/api/chat", json=payload)
        print(f"Chat endpoint: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Response preview: {result['response'][:100]}...")
            print(f"Sources found: {len(result['sources'])}")
        else:
            print(f"Error response: {response.text}")
    except Exception as e:
        print(f"Chat endpoint error: {e}")

if __name__ == "__main__":
    print("Testing RAG Agent API endpoints...")
    test_health_endpoint()
    test_root_endpoint()
    test_chat_endpoint()
    print("API testing completed.")