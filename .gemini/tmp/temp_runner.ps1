$featureDescription = @"
Spec1: URL Ingestion -> Embeddings -> Vector Store **Title:** Spec1 — Crawl book URLs, generate Cohere embeddings, store in Qdrant **Target audience:** Backend engineers building the RAG ingestion pipeline. **Focus:** Fetch published book pages, extract clean text, chunk content, generate Cohere embeddings, and upsert vectors with metadata into Qdrant Cloud. ## Success criteria - All provided URLs are fetched and processed (errors logged per-URL). - Text is chunked deterministically and embedded using Cohere. - Vectors and metadata are successfully stored in a Qdrant collection. - Re-running the pipeline does **not** create duplicate vectors (idempotent upserts). - Basic kNN search returns relevant chunks for test queries. - Logs report pages processed, chunks created, vectors stored, and failures.
"@

$scriptPath = "C:/Users/muhee/Desktop/Hackathon/Hackathon-HumanoidRobotics-book/.specify/scripts/powershell/create-new-feature.ps1"

& $scriptPath $featureDescription -Number 5 -ShortName "ingest-embeddings"