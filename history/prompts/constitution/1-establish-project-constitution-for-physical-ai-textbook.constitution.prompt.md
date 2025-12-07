## ---constitution---
id: 1
title: Establish Project Constitution for Physical AI Textbook
stage: constitution
date: 2025-12-07
surface: agent
model: Gemini
feature: none
branch: master
user: Muheeb Ali Jamali
command: /sp.constitution
labels: [constitution, project-setup]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
tests:
 - none
---

## Prompt

/sp.constitution 
  project_name: "Physical AI & Humanoid Robotics Textbook"

  purpose: """
  Define the principles, standards, constraints, and success criteria for producing a
  Docusaurus-based textbook for the Physical AI & Humanoid Robotics course. All outputs
  must be source-grounded, traceable, and fully reproducible.
  """

  core_principles: [
    "Accuracy: Content must strictly reflect user-provided textbook materials.",
    "Clarity: Explanations must remain accessible to learners in Physical AI and Humanoid Robotics.",
    "Reproducibility: Workflows must be repeatable using Spec-Kit Plus and Claude Code.",
    "Consistency: All chapters must follow uniform structure, formatting, and terminology.",
    "Source-Grounded Reasoning: No hallucinations; all claims must stem from provided sources."
  ]

  key_standards: [
    "All factual statements must derive from the textbook or specified references.",
    "Chapters must use Docusaurus-compliant Markdown.",
    "Content must be chunkable and index-ready for RAG.",
    "All agents/subagents must define deterministic I/O specifications."
  ]

  constraints: [
    "Markdown must remain fully Docusaurus-compatible.",
    "No unverifiable information may be introduced.",
    "Original textbook content must not be altered during retrieval.",
    "Frontend must support static deployment on GitHub Pages.",
    "All paths and scripts must remain PowerShell-compatible."
  ]

  success_criteria: [
    "The textbook builds and deploys on GitHub Pages without errors.",
    "RAG agents answer strictly from textbook-approved content.",
    "Chapters follow consistent structure, metadata, and indexing rules.",
    "All content is verifiable against the provided textbook.",
    "Versioning and project history are properly maintained."
  ]

## Response snapshot

I have updated the project constitution and ensured consistency across the relevant templates. The new constitution is at version 1.0.0.

## Outcome

- ✅ Impact: Project constitution established and aligned with templates.
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md and .specify/templates/plan-template.md
- 🔁 Next prompts: Suggest running /sp.specify to define a new feature.
- 🧠 Reflection: Adapting the user's input to the existing template structure was key.

## Evaluation notes (flywheel)

- Failure modes observed: The specified PHR creation script was not found, requiring a fallback to the agent-native flow.
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Verify the existence of scripts before attempting to execute them.
