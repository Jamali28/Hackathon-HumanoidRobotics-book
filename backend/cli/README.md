# RAG Testing CLI Tool

Professional command-line interface for testing the RAG chatbot end-to-end.

## Usage

### Basic Query
```bash
python cli/test_rag.py "What are the key concepts in humanoid robotics?"
```

### With Selected Text Context
```bash
python cli/test_rag.py "Explain this concept" --selected-text "Physical AI combines machine learning with physical systems to create intelligent robots that can interact with the real world."
```

### Custom API Endpoint
```bash
python cli/test_rag.py "How do robots learn?" --base-url http://my-server.com:8000
```

### Adjust Response Parameters
```bash
python cli/test_rag.py "What is embodied intelligence?" --temperature 0.9 --max-tokens 500
```

### Full Command Options
```bash
python cli/test_rag.py --help
```

## Features

- ✅ Sends queries to the `/api/chat` endpoint
- ✅ Displays model answers with proper formatting
- ✅ Shows retrieved sources with URL and chunk previews
- ✅ Supports optional `--selected-text` for contextual queries
- ✅ Configurable API base URL
- ✅ Professional logging and clear console output
- ✅ Error handling for connection issues
- ✅ No hardcoded URLs or mock data

## Example Output

```
2025-12-19 04:00:00,000 - INFO - Sending query to http://localhost:8000/api/chat
2025-12-19 04:00:00,000 - INFO - Query: What are the key concepts in humanoid robotics?
2025-12-19 04:00:00,000 - INFO - ✅ Query successful

🤖 Assistant Response:
   Humanoid robotics involves creating robots with human-like characteristics...

📋 Query:
   What are the key concepts in humanoid robotics?

🔗 Retrieved Sources (3):
   1. URL: https://example.com/humanoid-basics
      Score: 0.85
      Preview: Humanoid robotics is a branch of robotics focused on creating...
   2. URL: https://example.com/physical-ai
      Score: 0.72
      Preview: Physical AI combines machine learning with physical systems...
   3. URL: https://example.com/embodied-intelligence
      Score: 0.68
      Preview: Embodied intelligence refers to intelligence that emerges...
```

## Validation of RAG Correctness

Use this CLI tool to validate RAG correctness by:

1. **Source Attribution**: Verify that responses include relevant sources
2. **Context Relevance**: Check that answers are grounded in the retrieved content
3. **Response Quality**: Assess if answers are accurate and comprehensive
4. **Source Scores**: Evaluate if higher-scoring sources are more relevant
5. **Context Integration**: Test with `--selected-text` to ensure contextual understanding