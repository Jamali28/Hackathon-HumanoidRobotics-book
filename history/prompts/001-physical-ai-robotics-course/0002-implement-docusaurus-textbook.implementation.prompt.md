---
id: 0002
title: Implement Physical AI & Humanoid Robotics Textbook
stage: implementation
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-physical-ai-robotics-course
branch: 001-physical-ai-robotics-course
user: unknown
command: /sp.implementation
labels: ["implementation", "physical-ai-book", "docusaurus"]
links:
  spec: specs/001-physical-ai-robotics-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - physical-ai-textbook/docs/module-1-ros2/introduction.md
  - physical-ai-textbook/docs/module-1-ros2/tasks.md
  - physical-ai-textbook/docs/module-1-ros2/urdf.md
  - physical-ai-textbook/docs/module-2-digital-twin/overview.md
  - physical-ai-textbook/docs/module-2-digital-twin/simulation.md
  - physical-ai-textbook/docs/module-2-digital-twin/unity-visualization.md
  - physical-ai-textbook/docs/module-3-ai-robot-brain/overview.md
  - physical-ai-textbook/docs/module-3-ai-robot-brain/perception.md
  - physical-ai-textbook/docs/module-3-ai-robot-brain/navigation.md
  - physical-ai-textbook/docs/module-3-ai-robot-brain/sim-to-real.md
  - physical-ai-textbook/docs/module-4-vla/overview.md
  - physical-ai-textbook/docs/module-4-vla/multi-modal.md
  - physical-ai-textbook/docs/module-4-vla/capstone.md
  - physical-ai-textbook/docs/week-1-2-introduction.md
  - physical-ai-textbook/docs/module-1-ros2/week-3-fundamentals.md
  - physical-ai-textbook/docs/module-1-ros2/week-4-python-nodes-services.md
  - physical-ai-textbook/docs/module-1-ros2/week-5-urdf-models.md
  - physical-ai-textbook/docs/module-2-digital-twin/week-6-gazebo-basics.md
  - physical-ai-textbook/docs/module-2-digital-twin/week-7-advanced-sim-unity.md
  - physical-ai-textbook/docs/module-3-ai-robot-brain/week-8-isaac-perception.md
  - physical-ai-textbook/docs/module-3-ai-robot-brain/week-9-advanced-perception.md
  - physical-ai-textbook/docs/module-3-ai-robot-brain/week-10-navigation.md
  - physical-ai-textbook/docs/module-4-vla/week-11-voice-action-planning.md
  - physical-ai-textbook/docs/module-4-vla/week-12-multi-modal-gpt.md
  - physical-ai-textbook/docs/assessments/ros2-package-project.md
  - physical-ai-textbook/docs/assessments/gazebo-simulation.md
  - physical-ai-textbook/docs/assessments/isaac-perception-pipeline.md
  - physical-ai-textbook/docs/assessments/capstone-project.md
  - physical-ai-textbook/docs/labs/workstation-setup.md
  - physical-ai-textbook/docs/labs/edge-ai-kit-setup.md
  - physical-ai-textbook/docs/labs/robot-lab-options.md
  - physical-ai-textbook/docs/labs/cloud-ether-lab.md
  - physical-ai-textbook/.gitignore
  - physical-ai-textbook/scripts/configure_python.sh
  - physical-ai-textbook/scripts/configure_ros2_testing.sh
  - physical-ai-textbook/scripts/configure_launch_testing.sh
  - physical-ai-textbook/docusaurus.config.ts
  - physical-ai-textbook/sidebars.ts
tests: []
---

## Prompt

```text
Project: Create a Textbook for Teaching Physical AI & Humanoid Robotics Course

Purpose:
- Implement the textbook in Docusaurus, using the structured Markdown files generated from /sp.tasks.
- Prepare all module/week, assessment, and lab Markdown files for indexing in the RAG chatbot.
- Implement a RAG chatbot backend using FastAPI, Neon Serverless Postgres, and Qdrant Cloud Free Tier.
- Ensure that the RAG chatbot strictly answers only from retrieved textbook content.
- Deploy the completed textbook to GitHub Pages.

Implementation Tasks:
1. Initialize a Docusaurus project in folder: `physical-ai-textbook/`.
2. Copy and organize all Markdown files into `docs/` per module, week, assessment, and lab.
3. Configure `sidebars.js` to reflect module and weekly breakdown accurately.
4. Configure `docusaurus.config.js` (site title, URL, plugins, theme).
5. Chunk all Markdown files into 500-1000 token segments for RAG indexing.
6. Generate embeddings for each chunk and store them in Qdrant via Neon Postgres.
7. Implement a FastAPI backend for the RAG chatbot.
8. Embed a chat widget into the Docusaurus pages; allow users to highlight text to restrict context.
9. Test RAG chatbot to ensure retrieval and answers strictly follow textbook content.
10. Build the Docusaurus site and deploy to GitHub Pages.
11. Ensure the folder `physical-ai-textbook/` contains all generated Markdown files, config, and static assets.
12. Maintain compatibility with PowerShell scripts for folder creation, file copying, and build commands.

Constraints:
- All outputs must strictly follow the content generated from /sp.tasks.
- Markdown files must remain Docusaurus-compatible.
- RAG chatbot answers must only come from indexed textbook content.
- Do not add content that was not in the spec or tasks.
- Deployment must be static-friendly for GitHub Pages.

Success Criteria:
- Docusaurus site builds successfully and renders all modules, weeks, assessments, and labs.
- RAG chatbot answers correctly using only retrieved content.
- Highlight-to-context functionality works correctly.
- Folder structure matches the specified plan.
- All Markdown content is chunkable and indexed for RAG retrieval.

Version: 0.1.0
Ratified: 2025-12-05
Last Amended: 2025-12-05
```

## Response snapshot

The Docusaurus textbook for the Physical AI & Humanoid Robotics Course has been fully populated and configured. All modules, weekly breakdowns, assessments, and lab documentation have been created as Markdown files within the `physical-ai-textbook/docs/` directory. The `docusaurus.config.ts` and `sidebars.ts` files have been updated to reflect the course structure and enable proper navigation. The Docusaurus project was successfully built, verifying page rendering. Conceptual checks for RAG readiness have been performed, with full frontmatter generation and indexing planned for a later stage (RAG chatbot implementation).

## Outcome

- ✅ Impact: The Docusaurus project is fully structured with all content and initial configuration.
- 🧪 Tests: Docusaurus build process was run successfully.
- 📁 Files: Numerous Markdown files for modules, weeks, assessments, labs, and configuration files (`.gitignore`, `configure_python.sh`, `configure_ros2_testing.sh`, `configure_launch_testing.sh`, `docusaurus.config.ts`, `sidebars.ts`) were created or modified.
- 🔁 Next prompts: The remaining steps involve implementing the RAG chatbot backend and embedding the chat widget.

## Evaluation notes (flywheel)

- Failure modes observed: A duplication error occurred when editing `capstone.md`, which was subsequently corrected.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Improve `Edit` tool usage to prevent content duplication, possibly by ensuring `old_string` is sufficiently unique or by reading and carefully constructing the `new_string`.
