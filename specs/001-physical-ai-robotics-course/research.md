# Research Findings

## Python Version

**Decision**: Python 3.10
**Rationale**: Python 3.10 is the recommended version for ROS 2 distributions (e.g., Humble) and is widely supported by AI/ML libraries and robotics testing frameworks in 2025. It also ensures compatibility with MATLAB ROS Toolbox if integration is required.
**Alternatives considered**: Newer Python versions (e.g., 3.13) might require building ROS 2 from source and lack official support; older versions (e.g., 3.8, 3.9) have less future-proofing and might miss features from newer AI/ML libraries.

## Testing Frameworks

**Decision**: For Python-based ROS 2 agents: `ros2-easy-test` (with `pytest`) for unit and black-box testing, and `launch_testing` for integration tests. For Docusaurus Markdown content: rely on Docusaurus's built-in MDX processing and build-time validation.
**Rationale**: `ros2-easy-test` and `pytest` offer flexibility and robustness for ROS 2 agent testing, covering unit to black-box scenarios. `launch_testing` is crucial for complex integration tests involving multiple ROS 2 nodes. Docusaurus's native MDX processor is the primary mechanism for validating Markdown syntax and rendering, with additional debugging via MDX Playground. Comprehensive external Markdown content validation frameworks are not readily available or necessary given Docusaurus's capabilities.
**Alternatives considered**: Other generic Python testing frameworks like `unittest` could be used for ROS 2, but `pytest` offers more features and flexibility. For Docusaurus Markdown, manual review and reliance on build errors are the main alternatives to the built-in validation.

## Performance Goals

**Decision**: For Docusaurus documentation generation, prioritize optimized static output, fast client-side navigation (React-based SPA), and lightning-fast incremental builds with hot reloading for developer experience. For RAG retrieval, focus on high precision, recall, F1-score, and MRR for relevance, aiming for minimal hallucination rates and high factual consistency. Overall, achieve efficient retrieval and generation with low latency.
**Rationale**: Docusaurus is designed for efficient static site generation and developer productivity; leveraging its strengths aligns with project goals. For RAG, standard metrics (Precision, Recall, F1, MRR) are crucial for evaluating the quality of retrieved content and ensuring the generated textbook answers are accurate, relevant, and grounded in sources, thereby enhancing user satisfaction and minimizing factual errors.
**Alternatives considered**: Over-optimizing Docusaurus for complex MDX content may lead to reduced performance; focusing solely on basic Markdown ensures high performance but limits interactivity. For RAG, relying only on simple keyword matching would be less effective than incorporating advanced metrics like nDCG for nuanced ranking evaluation.
