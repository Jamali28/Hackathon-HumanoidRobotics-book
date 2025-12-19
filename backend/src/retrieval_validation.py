import os
import logging
import uuid
from typing import List, Dict, Tuple
from dotenv import load_dotenv
import cohere
from qdrant_client import QdrantClient, models
from qdrant_client.http.models import Filter, FieldCondition, MatchValue

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

class RAGRetrievalValidator:
    """
    Validates the RAG retrieval pipeline by querying the Qdrant vector store
    and verifying correctness, relevance, and stability of results.
    """

    def __init__(self):
        """Initialize the validator with Cohere and Qdrant clients."""
        self.cohere_api_key = os.getenv("COHERE_API_KEY")
        self.qdrant_url = os.getenv("QDRANT_URL")
        self.qdrant_api_key = os.getenv("QDRANT_API_KEY")

        if not all([self.cohere_api_key, self.qdrant_url, self.qdrant_api_key]):
            raise ValueError("Missing required environment variables: COHERE_API_KEY, QDRANT_URL, QDRANT_API_KEY")

        self.co = cohere.Client(self.cohere_api_key)
        self.client = QdrantClient(url=self.qdrant_url, api_key=self.qdrant_api_key)
        self.collection_name = "rag_embedding"

        logger.info("RAG Retrieval Validator initialized successfully.")

    def generate_query_embedding(self, query: str) -> List[float]:
        """
        Generate embeddings for a query using the same Cohere model as ingestion.

        Args:
            query: The query text to embed

        Returns:
            A list of floats representing the embedding vector
        """
        try:
            response = self.co.embed(
                texts=[query],
                model='embed-english-v3.0',  # Same model used during ingestion
                input_type='search_query'     # Specify this is a search query
            )
            embedding = response.embeddings[0]
            logger.info(f"Generated embedding for query (length: {len(query)}).")
            return embedding
        except Exception as e:
            logger.error(f"Error generating query embedding: {e}")
            raise

    def retrieve_chunks(self, query: str, top_k: int = 5) -> List[Dict]:
        """
        Retrieve relevant chunks from Qdrant based on the query embedding.

        Args:
            query: The query text
            top_k: Number of top results to retrieve

        Returns:
            List of dictionaries containing retrieved chunks with metadata
        """
        query_embedding = self.generate_query_embedding(query)

        try:
            # Perform semantic search in Qdrant
            search_results = self.client.query_points(
                collection_name=self.collection_name,
                query=query_embedding,
                limit=top_k,
                with_payload=True,
                with_vectors=False,
                score_threshold=0.3  # Only return results with similarity above threshold
            ).points

            retrieved_chunks = []
            for result in search_results:
                chunk_data = {
                    'id': result.id,
                    'score': result.score,
                    'text': result.payload.get('text', ''),
                    'source_url': result.payload.get('source_url', 'Unknown'),
                    'chunk_index': result.payload.get('chunk_index', -1),
                    'metadata': result.payload
                }
                retrieved_chunks.append(chunk_data)

            logger.info(f"Retrieved {len(retrieved_chunks)} chunks for query: '{query[:50]}...'")
            return retrieved_chunks

        except Exception as e:
            logger.error(f"Error retrieving chunks from Qdrant: {e}")
            raise

    def validate_relevance(self, query: str, retrieved_chunks: List[Dict]) -> Dict[str, float]:
        """
        Validate the relevance of retrieved chunks to the query.

        Args:
            query: Original query text
            retrieved_chunks: List of retrieved chunks with scores

        Returns:
            Dictionary with relevance metrics
        """
        if not retrieved_chunks:
            return {'avg_score': 0.0, 'relevant_ratio': 0.0, 'top_score': 0.0}

        scores = [chunk['score'] for chunk in retrieved_chunks]
        avg_score = sum(scores) / len(scores)
        top_score = max(scores) if scores else 0.0

        # Count chunks with high relevance (score > 0.5)
        high_relevance_threshold = 0.5
        relevant_count = sum(1 for score in scores if score > high_relevance_threshold)
        relevant_ratio = relevant_count / len(scores)

        return {
            'avg_score': avg_score,
            'relevant_ratio': relevant_ratio,
            'top_score': top_score,
            'total_retrieved': len(retrieved_chunks)
        }

    def validate_metadata_integrity(self, retrieved_chunks: List[Dict]) -> Dict[str, bool]:
        """
        Validate that retrieved chunks have correct metadata structure.

        Args:
            retrieved_chunks: List of retrieved chunks with metadata

        Returns:
            Dictionary with validation results
        """
        validation_results = {
            'has_source_url': True,  # Will be False if source_url is 'Unknown' (not saved during ingestion)
            'has_chunk_index': True,  # Will be False if chunk_index is -1 (not saved during ingestion)
            'has_text_content': True,
            'valid_ids': True,
            'valid_scores': True
        }

        for chunk in retrieved_chunks:
            # Check if required fields exist
            # Note: The ingestion pipeline currently only saves 'text' in the payload
            # source_url and chunk_index are not included in the current ingestion
            if not chunk.get('source_url') or chunk['source_url'] == 'Unknown':
                validation_results['has_source_url'] = False

            if chunk.get('chunk_index', -1) == -1:
                validation_results['has_chunk_index'] = False

            if not chunk.get('text') or len(chunk['text']) == 0:
                validation_results['has_text_content'] = False

            if not chunk.get('id'):
                validation_results['valid_ids'] = False

            if chunk.get('score', -1) < 0:
                validation_results['valid_scores'] = False

        return validation_results

    def run_consistency_test(self, query: str, num_runs: int = 3, top_k: int = 5) -> Dict:
        """
        Test retrieval consistency across multiple runs.

        Args:
            query: Query to test
            num_runs: Number of runs to perform
            top_k: Number of top results to retrieve

        Returns:
            Dictionary with consistency metrics
        """
        all_results = []
        all_scores = []

        for run in range(num_runs):
            logger.info(f"Consistency test run {run + 1}/{num_runs}")
            chunks = self.retrieve_chunks(query, top_k)
            all_results.append([chunk['id'] for chunk in chunks])
            all_scores.extend([chunk['score'] for chunk in chunks])

        # Calculate consistency metrics
        # Check if top result remains the same across runs
        top_results = [results[0] if results else None for results in all_results]
        unique_top_results = set(top_results)
        top_result_consistency = len(unique_top_results) == 1

        # Calculate score variance for the same chunks across runs
        avg_score_per_chunk = {}
        for run_results in all_results:
            for chunk_id in run_results:
                if chunk_id not in avg_score_per_chunk:
                    avg_score_per_chunk[chunk_id] = []

        # For simplicity in this implementation, we're just checking if the same
        # chunks are retrieved across runs, not comparing exact scores between runs
        # since Qdrant scores might vary slightly between identical searches

        consistency_metrics = {
            'runs_completed': num_runs,
            'top_result_consistent': top_result_consistency,
            'unique_top_results': len(unique_top_results),
            'total_unique_chunks': len(set([cid for run in all_results for cid in run])),
            'retrieval_success_rate': num_runs  # All runs completed successfully
        }

        return consistency_metrics

    def run_validation_suite(self, test_queries: List[str], top_k: int = 5) -> Dict:
        """
        Run a comprehensive validation suite for the retrieval pipeline.

        Args:
            test_queries: List of test queries to validate
            top_k: Number of top results to retrieve for each query

        Returns:
            Dictionary with comprehensive validation results
        """
        logger.info(f"Starting retrieval validation suite with {len(test_queries)} test queries...")

        validation_results = {
            'queries_tested': len(test_queries),
            'query_results': [],
            'overall_metrics': {
                'avg_avg_score': 0.0,
                'avg_relevant_ratio': 0.0,
                'total_chunks_retrieved': 0
            },
            'metadata_validation': {
                'has_source_url': True,
                'has_chunk_index': True,
                'has_text_content': True,
                'valid_ids': True,
                'valid_scores': True
            },
            'consistency_check': {}
        }

        total_avg_score = 0.0
        total_relevant_ratio = 0.0
        total_chunks = 0

        for i, query in enumerate(test_queries):
            logger.info(f"Testing query {i+1}/{len(test_queries)}: '{query}'")

            # Retrieve chunks
            retrieved_chunks = self.retrieve_chunks(query, top_k)
            total_chunks += len(retrieved_chunks)

            # Validate relevance
            relevance_metrics = self.validate_relevance(query, retrieved_chunks)
            total_avg_score += relevance_metrics['avg_score']
            total_relevant_ratio += relevance_metrics['relevant_ratio']

            # Validate metadata integrity
            metadata_valid = self.validate_metadata_integrity(retrieved_chunks)

            # Update overall metadata validation (AND operation)
            for key in validation_results['metadata_validation']:
                validation_results['metadata_validation'][key] &= metadata_valid[key]

            query_result = {
                'query': query,
                'relevance_metrics': relevance_metrics,
                'metadata_valid': metadata_valid,
                'sample_chunks': retrieved_chunks[:2]  # Include first 2 chunks as samples
            }

            validation_results['query_results'].append(query_result)

        # Calculate overall metrics
        if validation_results['queries_tested'] > 0:
            validation_results['overall_metrics']['avg_avg_score'] = \
                total_avg_score / validation_results['queries_tested']
            validation_results['overall_metrics']['avg_relevant_ratio'] = \
                total_relevant_ratio / validation_results['queries_tested']
            validation_results['overall_metrics']['total_chunks_retrieved'] = total_chunks

        # Run consistency test on the first query if available
        if test_queries:
            consistency_results = self.run_consistency_test(test_queries[0], num_runs=3, top_k=top_k)
            validation_results['consistency_check'] = consistency_results

        logger.info("Retrieval validation suite completed.")
        return validation_results

def main():
    """Main function to run the retrieval validation."""
    validator = RAGRetrievalValidator()

    # Define test queries that should retrieve relevant content
    test_queries = [
        "What are the key concepts in humanoid robotics?",
        "Explain physical AI and its importance",
        "How do robots learn from demonstrations?",
        "What are the hardware components for humanoid robots?",
        "Introduction to embodied AI systems"
    ]

    logger.info("Starting RAG retrieval validation...")

    # Run comprehensive validation suite
    results = validator.run_validation_suite(test_queries, top_k=5)

    # Print summary of results
    print("\n" + "="*60)
    print("RAG RETRIEVAL VALIDATION RESULTS")
    print("="*60)

    print(f"\nTested Queries: {results['queries_tested']}")
    print(f"Average Score Across All Queries: {results['overall_metrics']['avg_avg_score']:.3f}")
    print(f"Average Relevant Ratio: {results['overall_metrics']['avg_relevant_ratio']:.3f}")
    print(f"Total Chunks Retrieved: {results['overall_metrics']['total_chunks_retrieved']}")

    print(f"\nMetadata Validation:")
    for key, value in results['metadata_validation'].items():
        status = "PASS" if value else "FAIL"
        print(f"  {key}: {status}")

    print(f"\nConsistency Check:")
    print(f"  Runs Completed: {results['consistency_check'].get('runs_completed', 0)}")
    print(f"  Top Result Consistent: {results['consistency_check'].get('top_result_consistent', False)}")
    print(f"  Total Unique Chunks Retrieved: {results['consistency_check'].get('total_unique_chunks', 0)}")

    print(f"\nIndividual Query Results:")
    for i, query_result in enumerate(results['query_results'], 1):
        query = query_result['query']
        metrics = query_result['relevance_metrics']
        print(f"\n  Query {i}: '{query[:50]}{'...' if len(query) > 50 else ''}'")
        print(f"    Avg Score: {metrics['avg_score']:.3f}")
        print(f"    Relevant Ratio: {metrics['relevant_ratio']:.3f}")
        print(f"    Top Score: {metrics['top_score']:.3f}")
        print(f"    Chunks Retrieved: {metrics['total_retrieved']}")

        if query_result['sample_chunks']:
            sample = query_result['sample_chunks'][0]
            print(f"    Sample Chunk Score: {sample['score']:.3f}")
            print(f"    Sample Source: {sample['source_url'][:50]}...")

    print("\n" + "="*60)
    print("VALIDATION COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()