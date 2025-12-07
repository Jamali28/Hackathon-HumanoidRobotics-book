from typing import List, Dict, Optional
from pydantic import BaseModel, Field

class Metadata(BaseModel):
    source_path: str
    title: str
    module: Optional[str] = None
    week: Optional[int] = None
    keywords: List[str] = []
    headings: List[str] = []

class ContentChunk(BaseModel):
    chunk_id: str = Field(..., description="Unique identifier for the chunk.")
    chapter_id: str = Field(..., description="Unique ID of the source chapter.")
    content: str = Field(..., description="The actual text content of the chunk.")
    vector: List[float] = Field(..., description="The vector embedding of the content.")
    metadata: Metadata