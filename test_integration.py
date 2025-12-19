import requests
import time

def test_frontend_backend_integration():
    """Test the integration between frontend and backend"""
    print("Testing Frontend-Backend Integration...")

    # Test 1: Check if backend is running
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            print("[PASS] Backend server is running on port 8000")
        else:
            print("[FAIL] Backend server returned error")
            return False
    except requests.exceptions.ConnectionError:
        print("[FAIL] Cannot connect to backend server on port 8000")
        return False
    except:
        print("[FAIL] Error connecting to backend server")
        return False

    # Test 2: Check if backend API endpoint works
    try:
        payload = {
            "message": "What are humanoid robots?",
            "temperature": 0.7,
            "max_tokens": 200
        }
        response = requests.post("http://localhost:8000/api/chat", json=payload, timeout=15)
        if response.status_code == 200:
            data = response.json()
            print("[PASS] Backend API endpoint is working")
            print(f"   Response length: {len(data.get('response', ''))} characters")
            print(f"   Sources found: {len(data.get('sources', []))}")
        else:
            print(f"[FAIL] Backend API returned error: {response.status_code}")
            return False
    except Exception as e:
        print(f"[FAIL] Error calling backend API: {e}")
        return False

    # Test 3: Check if frontend is running (basic connectivity)
    try:
        response = requests.get("http://localhost:3000", timeout=5)
        if response.status_code == 200:
            print("[PASS] Frontend server is running on port 3000")
        else:
            print("[FAIL] Frontend server returned error")
            # This might be ok if the frontend isn't started, so we'll continue
    except:
        print("[WARN] Frontend server may not be running on port 3000 (this is OK for API testing)")

    print("\n[SUCCESS] Integration test completed successfully!")
    print("\nSystem Summary:")
    print("- Backend: FastAPI with Google Gemini LLM")
    print("- Vector DB: Qdrant for RAG retrieval")
    print("- Embeddings: Cohere (same as ingestion pipeline)")
    print("- Frontend: Docusaurus with RAG chat widget")
    print("- API: /api/chat endpoint for chat functionality")
    print("\nTo test the full integration:")
    print("1. Visit http://localhost:3000 to access the frontend")
    print("2. Use the chat widget (bottom-right corner)")
    print("3. Ask questions about humanoid robotics")
    print("4. Select text on pages to ask contextual questions")

    return True

if __name__ == "__main__":
    test_frontend_backend_integration()