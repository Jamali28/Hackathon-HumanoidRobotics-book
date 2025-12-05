## ---
id: 0001
title: Generate Tasks for Physical AI Textbook
stage: tasks
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: physical-ai-robotics-course
branch: 001-physical-ai-robotics-course
user: unknown
command: /sp.tasks
labels: ["tasks", "generation"]
links:
  spec: specs/001-physical-ai-robotics-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-physical-ai-robotics-course/tasks.md
tests: []
---

## Prompt

```text
Project: Physical AI & Humanoid Robotics Textbook (Docusaurus)

Purpose:
  - Generate detailed, actionable tasks for creating the textbook in Docusaurus.
  - Tasks should produce structured Markdown files for modules, weekly lessons, assessments, and hardware/lab instructions.
  - All outputs must be Docusaurus-compatible and ready for GitHub Pages deployment.

Task Generation Guidelines:
  - Base all tasks strictly on the provided course content.
  - Include task title, description, input, output, folder path, and dependencies.
  - Ensure each chapter/module/week is chunkable and index-ready for RAG agents.
  - Tasks should be traceable to course syllabus, modules, weekly breakdown, labs, and assessments.

Tasks:

- Task 1: Create Module Folders
  Description: Create folders for each module inside `./physical-ai-textbook/docs/`.
  Input: Course modules list
  Output: Folder structure:
    - `module-1-ros2/`
    - `module-2-digital-twin/`
    - `module-3-ai-robot-brain/`
    - `module-4-vla/`
  Folder: `./physical-ai-textbook/docs/`
  Dependencies: None

- Task 2: Write Module 1 Content (ROS 2)
  Description: Generate Markdown files covering:
    - Robotic nervous system
    - Nodes, Topics, Services
    - Python agent integration
    - URDF overview
  Input: Module 1 content
  Output: Markdown files in `module-1-ros2/`
  Folder: `./physical-ai-textbook/docs/module-1-ros2/`
  Dependencies: Task 1

- Task 3: Write Module 2 Content (Digital Twin)
  Description: Generate Markdown files covering:
    - Gazebo physics simulation
    - Unity environment building
    - Sensor simulation (LiDAR, Depth Cameras, IMUs)
    - High-fidelity rendering
  Input: Module 2 content
  Output: Markdown files in `module-2-digital-twin/`
  Folder: `./physical-ai-textbook/docs/module-2-digital-twin/`
  Dependencies: Task 1

- Task 4: Write Module 3 Content (AI-Robot Brain)
  Description: Generate Markdown files covering:
    - NVIDIA Isaac Sim
    - Isaac ROS, VSLAM
    - Path planning
    - AI-powered perception and manipulation
  Input: Module 3 content
  Output: Markdown files in `module-3-ai-robot-brain/`
  Folder: `./physical-ai-textbook/docs/module-3-ai-robot-brain/`
  Dependencies: Task 1

- Task 5: Write Module 4 Content (Vision-Language-Action)
  Description: Generate Markdown files covering:
    - Voice-to-Action with OpenAI Whisper
    - Cognitive planning using LLM → ROS 2 actions
    - Capstone: Autonomous Humanoid project
  Input: Module 4 content
  Output: Markdown files in `module-4-vla/`
  Folder: `./physical-ai-textbook/docs/module-4-vla/`
  Dependencies: Task 1

- Task 6: Add Weekly Breakdown
  Description: Generate weekly lesson pages (Weeks 1–13) in each module folder.
  Input: Weekly schedule
  Output: Markdown files for each week, including learning objectives and lab exercises
  Folder: `./physical-ai-textbook/docs/`
  Dependencies: Tasks 2–5

- Task 7: Add Assessments & Capstone
  Description: Create Markdown pages for:
    - ROS 2 package project
    - Gazebo simulation implementation
    - Isaac-based perception pipeline
    - Capstone humanoid robot project
  Input: Assessment details
  Output: Markdown files with instructions and grading rubric
  Folder: `./physical-ai-textbook/docs/assessments/`
  Dependencies: Tasks 2–6

- Task 8: Add Hardware & Lab Instructions
  Description: Generate Markdown files describing:
    - Workstation setup
    - Edge AI kits
    - Robot lab options (Proxy, Miniature, Premium)
    - Cloud Ether Lab
  Input: Hardware requirements
  Output: Markdown files in `./physical-ai-textbook/docs/labs/`
  Folder: `./physical-ai-textbook/docs/labs/`
  Dependencies: Tasks 2–6

- Task 9: Docusaurus Config & Navigation
  Description: Configure `sidebars.js` and `docusaurus.config.js` to reflect modules, weeks, assessments, and labs.
  Input: Folder structure and Markdown files
  Output: Navigation-ready Docusaurus configuration
  Folder: `./physical-ai-textbook/`
  Dependencies: Tasks 1–8

- Task 10: Test Build
  Description: Run Docusaurus build and verify all pages render correctly on GitHub Pages.
  Input: Full textbook folder
  Output: Validated static website
  Folder: `./physical-ai-textbook/`
  Dependencies: Task 9

Constraints:
  - Use only course-provided content; no hallucinations.
  - All Markdown must be compatible with Docusaurus and GitHub Pages.
  - Keep folder structure consistent for RAG indexing.
  - PowerShell-compatible paths and commands for Windows.

Success Criteria:
  - All modules, weeks, assessments, and labs are fully generated.
  - Docusaurus build completes successfully.
  - Textbook is ready for RAG integration.
  - Navigation and sidebar structure match course syllabus.

Version: 0.1.0
Ratified: 2025-12-05
Last Amended: 2025-12-05
```

## Response snapshot

The `tasks.md` file for the "Physical AI & Humanoid Robotics Course Textbook" has been successfully generated based on the provided user input and detailed planning guidelines. The tasks are organized into phases corresponding to user stories (P1, P2), foundational steps, and polish/cross-cutting concerns, ensuring independent implementability and testability. The file includes a total of 41 tasks, covering setup, module content creation, weekly breakdowns, assessments, hardware/lab instructions, and Docusaurus configuration and build.

## Outcome

- ✅ Impact: The project tasks have been successfully generated and structured, ready for implementation.
- 🧪 Tests: No automated tests were run for this operation.
- 📁 Files: `specs/001-physical-ai-robotics-course/tasks.md` was created.
- 🔁 Next prompts: The user has been provided with a summary of the generated tasks and an ADR suggestion will be made.

## Evaluation notes (flywheel)

- Failure modes observed: The `ls` command for checking existing PHRs failed due to the directory not existing. This was resolved by creating the directory with `mkdir -p`.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Incorporate a check for directory existence before `ls` in the PHR generation logic.
