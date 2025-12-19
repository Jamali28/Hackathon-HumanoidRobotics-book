# RAG Chatbot Integration - Complete System

This document provides an overview of the fully integrated RAG chatbot system combining frontend and backend components.

## System Architecture

```
┌─────────────────┐    HTTP/JSON     ┌──────────────────┐
│   Frontend      │ ──────────────►  │    Backend       │
│  (Docusaurus)   │                  │   (FastAPI)      │
│                 │                  │                  │
│ ┌─────────────┐ │                  │ ┌──────────────┐ │
│ │RAG Chat     │ │◄──── Text ───────┤ │RAG Agent     │ │
│ │Widget       │ │     Selection    │ │(Google Gemini)│ │
│ └─────────────┘ │                  │ └──────────────┘ │
│                 │                  │                  │
│ ┌─────────────┐ │   API Calls      │ ┌──────────────┐ │
│ │Docusaurus   │ │ ──────────────►  │ │Qdrant Vector │ │
│ │Pages        │ │                  │ │DB            │ │
│ └─────────────┘ │                  │ └──────────────┘ │
└─────────────────┘                  └──────────────────┘
```

## Components

### Backend (FastAPI)
- **Framework**: FastAPI
- **LLM**: Google Gemini (replacing OpenAI)
- **Vector DB**: Qdrant
- **Embeddings**: Cohere (consistent with ingestion pipeline)
- **API Endpoint**: `POST /api/chat`

### Frontend (Docusaurus)
- **Framework**: Docusaurus
- **Chat Widget**: Floating RAG-enabled chat interface
- **Text Selection**: Context-aware querying from selected text
- **API Integration**: HTTP communication with backend

## Setup Instructions

### Backend Setup
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in `.env`:
   ```env
   GEMINI_API_KEY=your_gemini_api_key
   COHERE_API_KEY=your_cohere_api_key
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_qdrant_api_key
   ```

4. Start the backend server:
   ```bash
   python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the frontend server:
   ```bash
   npx docusaurus start --port 3000
   ```

## Features

### RAG Chat Widget
- **Always Available**: Floating chat widget on every page
- **Contextual Queries**: Select text and ask questions about it
- **Source Attribution**: Responses include citations with relevance scores
- **Real-time Interaction**: Chat interface with loading states

### API Endpoints
- `GET /health` - Backend health check
- `GET /api/health` - Chat service health check
- `POST /api/chat` - Main chat endpoint with RAG capabilities

### Request Format
```json
{
  "message": "Your question here",
  "temperature": 0.7,
  "max_tokens": 1000
}
```

### Response Format
```json
{
  "response": "AI-generated response",
  "sources": [
    {
      "id": "chunk_id",
      "text": "source text snippet",
      "score": 0.85,
      "source_url": "source URL"
    }
  ],
  "query": "original query",
  "timestamp": "ISO timestamp"
}
```

## Environment Configuration

### Backend (.env)
```env
GEMINI_API_KEY=your_gemini_api_key
COHERE_API_KEY=your_cohere_api_key
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
```

### Frontend (.env)
```env
REACT_APP_RAG_API_URL=http://localhost:8000/api/chat
```

## Testing

### Backend API Test
```bash
cd backend
python test_api_connection.py
```

### Full Integration Test
```bash
python test_integration.py
```

## Key Improvements

1. **Gemini Integration**: Replaced OpenAI with Google Gemini for LLM capabilities
2. **Proper Error Handling**: Comprehensive error handling for API failures
3. **Source Attribution**: Proper citation of retrieved documents with scores
4. **Text Selection**: Context-aware querying from selected page text
5. **Responsive UI**: Modern, accessible chat interface

## Usage

1. Start both servers (backend on port 8000, frontend on port 3000)
2. Navigate to http://localhost:3000
3. Click the chat widget in the bottom-right corner
4. Ask questions about humanoid robotics
5. Select text on any page to ask contextual questions

## Troubleshooting

- **API Connection Issues**: Verify backend server is running and API URL is correct
- **CORS Errors**: Check backend CORS configuration
- **API Key Errors**: Ensure all required API keys are set in environment variables
- **Qdrant Connection**: Verify Qdrant URL and API key are correct

## Performance Notes

- The system leverages pre-computed embeddings for fast retrieval
- Response times depend on LLM API performance
- Caching can be implemented for frequently asked questions
- Vector search performance scales with collection size