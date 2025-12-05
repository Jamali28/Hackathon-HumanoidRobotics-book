<!-- Sync Impact Report:
Version change:  → 0.1.0
Modified principles:
  - [PROJECT_NAME] -> Create a Textbook for Teaching Physical AI & Humanoid Robotics Course
  - [PRINCIPLE_1_NAME] -> Accuracy
  - [PRINCIPLE_2_NAME] -> Clarity
  - [PRINCIPLE_3_NAME] -> Reproducibility
  - [PRINCIPLE_4_NAME] -> Consistency
  - [PRINCIPLE_5_NAME] -> Source-Grounded Reasoning
Added sections:
  - Key Standards
  - Constraints
  - Success Criteria
Removed sections:
  - PRINCIPLE_6_NAME and PRINCIPLE__DESCRIPTION placeholders
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
  - .specify/templates/commands/*.md: ⚠ pending
Follow-up TODOs: none
-->
# Create a Textbook for Teaching Physical AI & Humanoid Robotics Course Constitution

## Core Principles

### Accuracy
All content must be strictly based on the textbook material provided.

### Clarity
Content must be understandable for learners in Physical AI, Humanoid Robotics, and related engineering fields.

### Reproducibility
Workflows must be reproducible across Spec-Kit Plus + Claude Code.

### Consistency
Chapters must maintain uniform structure, formatting, and technical definitions.

### Source-Grounded Reasoning
No hallucinations; all content is sourced from textbook material or user-supplied references.

## Key Standards

- All factual statements must originate from provided textbook content or explicitly supplied sources.
- All chapters must follow a unified markdown template compatible with Docusaurus.
- All content must be chunkable and index-ready for RAG retrieval.
- RAG chatbot answers must rely only on retrieved content or user-selected text.
- Agents and subagents must have clear input/output specifications and deterministic behavior.

## Constraints

- Markdown must remain Docusaurus-compatible.
- No external unverifiable facts or assumptions may be introduced.
- Original chapter content cannot be modified during retrieval or RAG generation.
- Frontend must remain static-friendly for deployment on GitHub Pages.
- PowerShell-compatible paths and scripts must be used; no bash-only commands.


## Success Criteria

- Textbook builds and deploys successfully to GitHub Pages.
- RAG chatbot answers strictly from textbook content.
- Chapters maintain uniform structure, metadata, and indexing.
- All content is verifiable against the textbook; no hallucinations.
- Project history and versioning maintained via `.specify/history/constitution/`.

**Version**: 0.1.0 | **Ratified**: 2025-12-05 | **Last Amended**: 2025-12-05
