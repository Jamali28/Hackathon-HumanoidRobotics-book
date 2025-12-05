## ---
id: 0002
title: Create Feature Specification
stage: spec
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: 001-physical-ai-robotics-course
branch: 001-physical-ai-robotics-course
user: unknown
command: /sp.specify
labels: ["spec", "feature-creation"]
links:
  spec: specs/001-physical-ai-robotics-course/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-physical-ai-robotics-course/spec.md
  - specs/001-physical-ai-robotics-course/checklists/requirements.md
tests: []
---

## Prompt

```text
Project: Create a Textbook for Teaching Physical AI & Humanoid Robotics Course

Purpose:
  - Generate structured specifications, plans, and tasks for the Physical AI & Humanoid Robotics course.
  - Base all outputs strictly on provided course content: modules, weekly breakdown, lab/hardware requirements, assessments, and capstone.
  - Ensure generated content is actionable for instructors, developers, and Claude Code agents.

Course Details:
  Title: Physical AI & Humanoid Robotics
  Focus: AI Systems in the Physical World; Embodied Intelligence
  Goal: Bridge the digital brain and physical body; apply AI knowledge to control humanoid robots in simulated and real environments.

Modules:
  - Module 1: Robotic Nervous System (ROS 2)
    Topics: Nodes, Topics, Services, Python agents, URDF
  - Module 2: Digital Twin (Gazebo & Unity)
    Topics: Physics simulation, collisions, LiDAR, Depth Cameras, IMUs, Unity visualization
  - Module 3: AI-Robot Brain (NVIDIA Isaac™)
    Topics: Isaac Sim, Isaac ROS, VSLAM, path planning
  - Module 4: Vision-Language-Action (VLA)
    Topics: Voice-to-Action (Whisper), Cognitive Planning (LLM → ROS 2 actions), Capstone: Autonomous Humanoid

Weekly Breakdown:
  - Weeks 1-2: Introduction to Physical AI, sensors, humanoid robotics landscape
  - Weeks 3-5: ROS 2 fundamentals and Python integration
  - Weeks 6-7: Gazebo simulation, URDF/SDF, physics and sensors
  - Weeks 8-10: NVIDIA Isaac: perception, manipulation, sim-to-real
  - Weeks 11-12: Humanoid robot development: kinematics, locomotion, manipulation
  - Week 13: Conversational robotics: GPT integration, speech, multi-modal interaction

Assessments:
  - ROS 2 package development project
  - Gazebo simulation implementation
  - Isaac-based perception pipeline
  - Capstone: Simulated humanoid robot with conversational AI

Hardware Requirements:
  - High-performance workstation with NVIDIA RTX 4070 Ti+ (3090/4090 preferred), Core i7 13th Gen+ / Ryzen 9, 64GB RAM, Ubuntu 22.04
  - Edge AI kit: Jetson Orin Nano/NX, Intel RealSense D435i, USB IMU (BNO055), USB microphone/speaker
  - Robot Lab options: Proxy robot (Unitree Go2 Edu), Miniature humanoid (Unitree G1/Robotis OP3/Hiwonder TonyPi), Premium humanoid (Unitree G1)
  - Cloud Ether Lab optional: AWS/Azure instances, Jetson kit still required

Constraints:
  - Generate tasks, plans, and specifications strictly from provided course content.
  - Tasks must be actionable, chunkable, and indexable for RAG agents.
  - Maintain Docusaurus-compatible markdown structure for all outputs.
  - Hardware and lab setups must match course description exactly; no assumptions.
  - Capstone tasks must reflect the sequence: voice command → planning → navigation → perception → manipulation.

Success Criteria:
  - All modules, weeks, and assessments are mapped to actionable tasks.
  - Each task can be traced back to course content.
  - Plans and specifications are clear for instructors and agents.
  - Generated outputs are ready to integrate into the textbook.
  - RAG agents retrieve only from indexed course data.

Version: 0.1.0
Ratified: 2025-12-05
Last Amended: 2025-12-05
```

## Response snapshot

The feature specification for "Physical AI & Humanoid Robotics Course Textbook" has been successfully created. The branch `001-physical-ai-robotics-course` was created, and the spec file is located at `specs/001-physical-ai-robotics-course/spec.md`. All specification quality checks passed, and the feature is ready for the planning phase.

## Outcome

- ✅ Impact: The feature specification has been successfully generated and validated according to the provided course details.
- 🧪 Tests: No automated tests were run as part of specification generation.
- 📁 Files: `specs/001-physical-ai-robotics-course/spec.md` and `specs/001-physical-ai-robotics-course/checklists/requirements.md` were created/modified.
- 🔁 Next prompts: The next step is to proceed with `/sp.plan` to generate an implementation plan.
- 🧠 Reflection: The agent successfully parsed complex user input to create a structured specification. The PowerShell script error during branch creation was identified as a parameter binding issue, but the branch and spec file creation itself was successful. The agent correctly identified the existing branch and continued with the subsequent steps.

## Evaluation notes (flywheel)

- Failure modes observed: The `create-new-feature.ps1` script encountered a `ParameterBindingException` when executed via `powershell.exe -File`, indicating an issue with how the long, multi-line feature description was passed as a positional argument. The `create-phr.sh` script was not found, requiring agent-native PHR creation.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Investigate robust ways to pass long, multi-line strings as positional arguments to PowerShell scripts from the Bash environment, or consider alternative input methods for the script. Ensure the `create-phr.sh` script is available or update the instructions to consistently use agent-native PHR creation.
