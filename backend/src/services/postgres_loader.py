import os
import psycopg2
from typing import List
from backend.src.models.rag_models import ContentChunk

NEON_PG_CONN_STRING = os.getenv("NEON_PG_CONN_STRING")

def get_postgres_connection():
    if not NEON_PG_CONN_STRING:
        raise ValueError("NEON_PG_CONN_STRING environment variable not set.")
    conn = psycopg2.connect(NEON_PG_CONN_STRING)
    return conn

def create_chunks_table_if_not_exists(conn):
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS content_chunks (
                chunk_id VARCHAR(255) PRIMARY KEY,
                chapter_id VARCHAR(255),
                content TEXT,
                source_path VARCHAR(512),
                title VARCHAR(255),
                module VARCHAR(255),
                week INTEGER,
                keywords TEXT[],
                headings TEXT[]
            );
        """)
        conn.commit()
    print("Content chunks table ensured to exist in Postgres.")

def insert_chunks_to_postgres(conn, chunks: List[ContentChunk]):
    with conn.cursor() as cur:
        for chunk in chunks:
            cur.execute("""
                INSERT INTO content_chunks (
                    chunk_id, chapter_id, content,
                    source_path, title, module, week, keywords, headings
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (chunk_id) DO UPDATE SET
                    chapter_id = EXCLUDED.chapter_id,
                    content = EXCLUDED.content,
                    source_path = EXCLUDED.source_path,
                    title = EXCLUDED.title,
                    module = EXCLUDED.module,
                    week = EXCLUDED.week,
                    keywords = EXCLUDED.keywords,
                    headings = EXCLUDED.headings;
            """, (
                chunk.chunk_id,
                chunk.chapter_id,
                chunk.content,
                chunk.metadata.source_path,
                chunk.metadata.title,
                chunk.metadata.module,
                chunk.metadata.week,
                chunk.metadata.keywords,
                chunk.metadata.headings
            ))
        conn.commit()
    print(f"Inserted/Updated {len(chunks)} chunks in Postgres.")

if __name__ == "__main__":
    # Example usage:
    # Requires NEON_PG_CONN_STRING to be set as an environment variable.
    # Replace dummy_chunks with actual chunks from chunking.py

    # Dummy chunks (replace with actual chunks from chunking.py)
    dummy_chunks = [
        ContentChunk(
            chunk_id="intro-0",
            chapter_id="introduction",
            content="This is the first part of the introduction.",
            vector=[0.1] * 768, # Vector not stored in Postgres, but part of ContentChunk model
            metadata={
                "source_path": "frontend/docs/introduction.md",
                "title": "Introduction",
                "keywords": ["intro", "course"],
                "headings": ["Introduction"]
            }
        ),
        ContentChunk(
            chunk_id="intro-1",
            chapter_id="introduction",
            content="This is the second part, discussing physical AI concepts.",
            vector=[0.2] * 768,
            metadata={
                "source_path": "frontend/docs/introduction.md",
                "title": "Introduction",
                "keywords": ["physical ai", "concepts"],
                "headings": ["Physical AI Concepts"]
            }
        )
    ]

    try:
        conn = get_postgres_connection()
        create_chunks_table_if_not_exists(conn)
        insert_chunks_to_postgres(conn, dummy_chunks)
        conn.close()
    except Exception as e:
        print(f"Error during Postgres operations: {e}")
