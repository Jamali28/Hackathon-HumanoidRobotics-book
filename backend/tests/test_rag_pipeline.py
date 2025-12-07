import pytest
from unittest.mock import MagicMock, patch
from backend.src.services.chunking import chunk_markdown
from backend.src.models.rag_models import ContentChunk, Metadata
from backend.src.api.main import app
from fastapi.testclient import TestClient

# Mock data for testing
MOCK_MARKDOWN_CONTENT = """
---
id: test-chapter
title: Test Chapter Title
keywords: [test, mock]
---
# Main Heading
## Sub Heading
This is some test content.
Another paragraph.
"""

MOCK_METADATA = {
    "id": "test-chapter",
    "title": "Test Chapter Title",
    "keywords": ["test", "mock"]
}

@pytest.fixture
def mock_file_read(tmp_path):
    # Create a dummy markdown file for chunking test
    file_path = tmp_path / "test_chapter.md"
    file_path.write_text(MOCK_MARKDOWN_CONTENT)
    return str(file_path)

@pytest.fixture
def client():
    # Setup test client for FastAPI app
    return TestClient(app)

# Test chunking pipeline
def test_chunk_markdown(mock_file_read):
    chunks = chunk_markdown(mock_file_read, MOCK_METADATA['id'], MOCK_METADATA['title'], MOCK_METADATA)
    assert len(chunks) > 0
    assert isinstance(chunks[0], ContentChunk)
    assert chunks[0].chapter_id == MOCK_METADATA['id']
    assert chunks[0].metadata.title == MOCK_METADATA['title']
    assert "Main Heading" in chunks[0].content
    assert chunks[0].vector == [0.0] * 768 # Should be placeholder vector

# Test FastAPI endpoint
@patch('backend.src.api.main.RAGAgent') # Mock the RAGAgent if imported
def test_query_rag_system(mock_rag_agent_class, client):
    # Mock RAGAgent instance and its query method
    mock_rag_agent_instance = MagicMock()
    mock_rag_agent_instance.query.return_value = {
        "answer": "Mocked answer for test query.",
        "sources": [
            {
                "chunk_id": "mock-chunk-1",
                "content": "Mocked source content.",
                "metadata": {"source_path": "mock/path.md", "title": "Mock Title"}
            }
        ]
    }
    mock_rag_agent_class.return_value = mock_rag_agent_instance

    response = client.post("/api/v1/query", json={"query": "What is ROS 2?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "sources" in data
    assert data["answer"] == "Mocked answer for test query."
    assert len(data["sources"]) > 0
    assert data["sources"][0]["chunk_id"] == "mock-chunk-1"
