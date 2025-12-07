<!-- 
Sync Impact Report:
- Version change: 0.0.0 -> 1.0.0
- Modified principles: All principles have been updated.
- Added sections: Key Standards, Constraints, Success Criteria
- Removed sections: None
- Templates requiring updates:
  - ✅ .specify/templates/plan-template.md
  - ✅ .specify/templates/spec-template.md
  - ✅ .specify/templates/tasks-template.md
- Follow-up TODOs: None
-->

# Physical AI & Humanoid Robotics Textbook Constitution

## Purpose

Define the principles, standards, constraints, and success criteria for producing a
Docusaurus-based textbook for the Physical AI & Humanoid Robotics course. All outputs
must be source-grounded, traceable, and fully reproducible.

## Core Principles

### I. Accuracy
Content must strictly reflect user-provided textbook materials.

### II. Clarity
Explanations must remain accessible to learners in Physical AI and Humanoid Robotics.

### III. Reproducibility
Workflows must be repeatable using Spec-Kit Plus and Claude Code.

### IV. Consistency
All chapters must follow uniform structure, formatting, and terminology.

### V. Source-Grounded Reasoning
No hallucinations; all claims must stem from provided sources.

## Key Standards

- All factual statements must derive from the textbook or specified references.
- Chapters must use Docusaurus-compliant Markdown.
- Content must be chunkable and index-ready for RAG.
- All agents/subagents must define deterministic I/O specifications.

## Constraints

- Markdown must remain fully Docusaurus-compatible.
- No unverifiable information may be introduced.
- Original textbook content must not be altered during retrieval.
- Frontend must support static deployment on GitHub Pages.
- All paths and scripts must remain PowerShell-compatible.

## Success Criteria

- The textbook builds and deploys on GitHub Pages without errors.
- RAG agents answer strictly from textbook-approved content.
- Chapters follow consistent structure, metadata, and indexing rules.
- All content is verifiable against the provided textbook.
- Versioning and project history are properly maintained.

## Governance

This Constitution defines the project's foundational principles. It is the authoritative source for all development standards, architectural decisions, and quality assurance. All contributors, tools, and processes must adhere to these principles. Amendments require review and approval to ensure they align with the project's core purpose.

**Version**: 1.0.0 | **Ratified**: 2025-12-07 | **Last Amended**: 2025-12-07