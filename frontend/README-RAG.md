# RAG Chatbot Integration

This document explains how to run the Docusaurus frontend with the RAG backend for the chatbot functionality.

## Prerequisites

- Node.js (v16 or higher)
- Python 3.8+
- Access to OpenAI API key
- Access to Cohere API key
- Access to Qdrant vector database

## Setup Instructions

### 1. Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd ../backend
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables by creating a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   COHERE_API_KEY=your_cohere_api_key
   QDRANT_URL=your_qdrant_url
   QDRANT_API_KEY=your_qdrant_api_key
   ```

4. Run the FastAPI backend:
   ```bash
   python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
   ```

### 2. Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd ../frontend  # or wherever your frontend is located
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. The `.env` file is already configured to point to the backend:
   ```
   REACT_APP_RAG_API_URL=http://localhost:8000/api/chat
   ```

4. Start the Docusaurus development server:
   ```bash
   npm run start
   ```

## Features

### Chat Widget
- The chat widget appears as a floating button on the bottom-right of every page
- Click the button to open the chat interface
- The widget maintains conversation history within each session

### Text Selection
- Select any text on a page and then open the chat widget
- The selected text will be automatically included in your query context
- A visual indicator shows that the selected text is being used

### Source Attribution
- Responses include source citations with relevance scores
- Click on "Sources" to expand and view the source chunks used
- Source links allow direct navigation to original content

## API Communication

The frontend communicates with the backend through the `/api/chat` endpoint:
- Request format: `{ message: string, temperature: number, max_tokens: number }`
- Response format: `{ response: string, sources: SourceChunk[], query: string, timestamp: string }`
- SourceChunk format: `{ id: string, text: string, score: number, source_url: string }`

## Troubleshooting

### CORS Issues
If you encounter CORS errors, make sure your FastAPI backend has the proper CORS middleware configured.

### API Connection Issues
- Verify that the backend server is running on the configured port
- Check that the `REACT_APP_RAG_API_URL` in `.env` matches your backend URL
- Ensure your firewall allows communication between the frontend and backend ports

### Environment Variables
- Make sure all required API keys are properly set in the backend `.env` file
- The frontend only requires the API URL configuration

## Development

For local development, both servers should run simultaneously:
- Backend: `python -m uvicorn src.main:app --host 0.0.0.0 --port 8000`
- Frontend: `npm run start`

The chat widget will be available on every page of your Docusaurus site.