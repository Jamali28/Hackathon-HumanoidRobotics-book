import requests
import json

# Test the chat endpoint with a simple query
url = "http://localhost:8000/api/chat"
payload = {
    "message": "Hello",
    "temperature": 0.7,
    "max_tokens": 200
}

print("Testing chat endpoint with simple query...")
print(f"URL: {url}")
print(f"Payload: {json.dumps(payload, indent=2)}")

try:
    response = requests.post(url, json=payload, timeout=30)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")

    if response.status_code == 200:
        try:
            data = response.json()
            print(f"Response JSON: {json.dumps(data, indent=2)}")
        except:
            print("Response is not valid JSON")
    else:
        print("Error occurred - checking server logs...")

except requests.exceptions.Timeout:
    print("Request timed out - server might be processing slowly or hung")
except requests.exceptions.ConnectionError:
    print("Cannot connect to server - is it running?")
except Exception as e:
    print(f"Exception occurred: {e}")