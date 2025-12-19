from pydantic import BaseModel
from typing import List, Optional


class ChatRequest(BaseModel):
    message: str
    temperature: Optional[float] = 0.7
    max_tokens: Optional[int] = 1000


class SourceChunk(BaseModel):
    id: str
    text: str
    score: float
    source_url: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    sources: List[SourceChunk]
    query: str
    timestamp: str