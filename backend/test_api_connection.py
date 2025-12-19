import requests
import json
import time

def test_backend_api():
    """Test the backend API endpoint"""
    print("Testing backend API connection...")

    # Test data
    test_payload = {
        "message": "What are the key concepts in humanoid robotics?",
        "temperature": 0.7,
        "max_tokens": 200
    }

    try:
        # Make request to the backend
        response = requests.post(
            'http://localhost:8000/api/chat',
            json=test_payload,
            timeout=30  # 30 second timeout
        )

        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            print("[PASS] API connection successful!")
            print(f"Response keys: {list(data.keys())}")
            print(f"Response length: {len(data.get('response', ''))} characters")
            print(f"Sources found: {len(data.get('sources', []))}")
            return True
        else:
            print(f"[FAIL] API returned error: {response.status_code}")
            print(f"Response: {response.text}")
            return False

    except requests.exceptions.ConnectionError:
        print("[FAIL] Cannot connect to backend server. Is it running on port 8000?")
        return False
    except requests.exceptions.Timeout:
        print("[FAIL] Request timed out. Backend might be processing slowly.")
        return False
    except Exception as e:
        print(f"[FAIL] Error testing API: {str(e)}")
        return False

def test_health_check():
    """Test the health check endpoint"""
    print("\nTesting health check endpoint...")

    try:
        response = requests.get('http://localhost:8000/health', timeout=10)
        print(f"Health check status: {response.status_code}")

        if response.status_code == 200:
            print("[PASS] Health check successful!")
            return True
        else:
            print(f"[FAIL] Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"[FAIL] Error testing health check: {str(e)}")
        return False

if __name__ == "__main__":
    print("Starting RAG Backend API Test\n")

    # Test health check first
    health_ok = test_health_check()

    # Wait a moment before testing the main endpoint
    time.sleep(2)

    # Test the main chat endpoint
    api_ok = test_backend_api()

    print(f"\nTest Results:")
    print(f"Health Check: {'[PASS]' if health_ok else '[FAIL]'}")
    print(f"API Endpoint: {'[PASS]' if api_ok else '[FAIL]'}")

    if health_ok and api_ok:
        print("\n[SUCCESS] All tests passed! Backend is ready for frontend integration.")
    else:
        print("\n[WARNING] Some tests failed. Please check the backend configuration.")
        print("Note: If the API Endpoint failed with 'GEMINI_API_KEY environment variable is required',")
        print("      you need to set the GEMINI_API_KEY in your environment or .env file.")