# Spec3 Implementation Plan: RAG Agent Backend with OpenAI Agents SDK

## Overview
Build an AI agent that uses OpenAI Agents SDK with retrieval tools backed by Qdrant, exposed via a FastAPI service to answer questions about the book content.

## Architecture
- FastAPI backend service
- OpenAI Agents SDK for AI orchestration
- Qdrant vector database for retrieval
- Cohere embeddings for consistency with ingestion

## Implementation Steps

### 1. Setup and Dependencies
- Initialize FastAPI app
- Add required dependencies (openai, fastapi, uvicorn, pydantic, cohere, qdrant-client)
- Set up environment configuration

### 2. Retrieval Service
- Create a retrieval service class that queries Qdrant
- Use the same embedding model as ingestion (Cohere embed-english-v3.0)
- Implement query processing and chunk retrieval
- Handle empty retrieval cases gracefully

### 3. OpenAI Agent Configuration
- Set up OpenAI Assistant with retrieval tool
- Create tool definition for RAG functionality
- Configure agent to use retrieved context
- Handle response formatting with sources

### 4. FastAPI Endpoints
- Create `/chat` endpoint for user queries
- Implement request/response models
- Add error handling and validation
- Include source citation in responses

### 5. Integration and Testing
- Connect all components
- Test end-to-end flow
- Validate response quality and source attribution
- Handle edge cases (no results, errors, etc.)

## File Structure
```
backend/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── rag_agent.py
│   │   └── retrieval_tool.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── chat_router.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── retrieval_service.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── request_response.py
│   └── main.py
├── requirements.txt
└── .env.example
```

## Success Criteria Verification
- [ ] Agent accepts user queries via FastAPI endpoint
- [ ] Query embeddings generated and chunks retrieved from Qdrant
- [ ] Retrieved context injected into agent's prompt/tool flow
- [ ] Agent responses grounded in retrieved content
- [ ] API returns structured, stable responses with sources