# Actionable Tasks for: Docusaurus Textbook

**Branch**: `001-docusaurus-textbook` | **Date**: 2025-12-07 | **Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md)

This task list is derived from the feature specification and implementation plan. Tasks are organized by user story to facilitate independent, parallel, and testable development.

## Phase 1: Setup

- [x] T001 Create project monorepo structure with `frontend/` and `backend/` directories.
- [x] T002 Initialize a Docusaurus project in the `frontend/` directory.
- [x] T003 Initialize a Python project with a virtual environment in the `backend/` directory.
- [x] T004 [P] Create `backend/requirements.txt` with FastAPI, Uvicorn, Qdrant-client, psycopg2-binary, and OpenAI.
- [x] T005 [P] Set up a `.gitignore` file for Node.js and Python projects.

## Phase 2: Foundational Tasks

- [x] T006 [P] Configure basic Docusaurus settings in `frontend/docusaurus.config.js` (e.g., project title, theme).
- [x] T007 [P] Create initial directory structure for content in `frontend/docs/` (e.g., `modules/`, `weeks/`, `hardware/`, `assessments/`).

## Phase 3: User Story 1 - Learner Accesses Curriculum Content

**Story Goal**: A learner can navigate the Docusaurus textbook to access the curriculum content.
**Independent Test**: The Docusaurus site can be built and served locally, and a user can navigate to all generated content pages.

- [x] T008 [US1] Generate the Course Introduction chapter at `frontend/docs/introduction.md`.
- [x] T009 [P] [US1] Generate Module 1-4 chapters in `frontend/docs/modules/`.
- [x] T010 [P] [US1] Generate Weeks 1-13 chapters in `frontend/docs/weeks/`.
- [x] T011 [US1] Configure the navigation bar in `frontend/docusaurus.config.js` to include top-level sections.
- [x] T012 [US1] Configure the sidebar in `frontend/sidebars.js` to create a hierarchy for modules and weeks.
- [x] T013 [US1] Implement the homepage hero section in `frontend/src/pages/index.js`.
- [x] T014 [P] [US1] Enable and configure the dark mode toggle in `frontend/docusaurus.config.js`.

## Phase 4: User Story 2 - RAG Chatbot Retrieves Specific Content

**Story Goal**: A chatbot can retrieve specific content from the textbook via a backend API.
**Independent Test**: The FastAPI backend can be run, and a query to the `/api/v1/query` endpoint returns a valid response based on ingested data.

- [x] T015 [US2] Implement the `ContentChunk` and `Metadata` data models in `backend/src/models/`.
- [x] T016 [US2] Create the content chunking pipeline script at `backend/src/services/chunking.py`.
- [x] T017 [US2] Implement the Qdrant and Neon Postgres loader scripts in `backend/src/services/`.
- [x] T018 [US2] Create the FastAPI application and the `/api/v1/query` endpoint in `backend/src/api/main.py`.
- [x] T019 [US2] Implement the RAG agent logic for querying and response generation in `backend/src/services/agent.py`.
- [x] T020 [P] [US2] Add unit tests for the chunking and API logic in `backend/tests/`.

## Phase 5: User Story 3 - Developer Builds and Deploys the Textbook

**Story Goal**: A developer can build and deploy the Docusaurus textbook to GitHub Pages.
**Independent Test**: Running the build command successfully generates the static site, and the deployment script successfully pushes it to the `gh-pages` branch.

- [x] T021 [US3] Configure the deployment settings in `frontend/docusaurus.config.js` for GitHub Pages.
- [x] T022 [US3] Create a GitHub Actions workflow file at `.github/workflows/deploy.yml` to automate the build and deployment.
- [x] T023 [P] [US3] Add documentation for the deployment process in `README.md`.

## Phase 6: User Story 4 - Learner Reviews Assessments and Hardware

**Story Goal**: A learner can find detailed information on assessments and hardware.
**Independent Test**: The assessment and hardware pages are present on the deployed site and contain the correct content.

- [x] T024 [P] [US4] Generate hardware and lab architecture chapters in `frontend/docs/hardware/`.
- [x] T025 [P] [US4] Generate assessments and capstone chapters in `frontend/docs/assessments/`.

## Phase 7: Polish & Cross-Cutting Concerns

- [x] T026 Add custom CSS for responsive tables in `frontend/src/css/custom.css`.
- [x] T027 Implement the floating chatbot placeholder component in `frontend/src/theme/Root.js`.
- [x] T028 Perform a final validation of all links and content.

## Dependency Graph
- **Phase 1 & 2** must be completed before other phases.
- **Phase 3 (US1)** is a prerequisite for **Phase 4 (US2)**, as content must exist to be indexed.
- **Phase 5 (US3)** can be worked on in parallel with other phases after Phase 1.
- **Phase 6 (US4)** is a content-only task that can be done in parallel with Phase 3.

## Parallel Execution Examples
- **Per User Story**:
  - In Phase 3 (US1), `T009` and `T010` (content generation) can be done in parallel.
  - In Phase 4 (US2), `T017` (data loaders) and `T020` (unit tests) can be started once the models in `T015` are defined.
- **Across User Stories**:
  - Phase 5 (US3) can start as soon as the Docusaurus project is initialized in Phase 1.
  - Phase 6 (US4) can be worked on at the same time as Phase 3.

## Implementation Strategy
The implementation will follow an MVP-first approach. The primary goal is to complete all tasks for User Story 1 to deliver a readable, navigable textbook. This will serve as the MVP. Subsequent user stories (RAG backend, deployment automation) will be implemented as incremental feature additions.
