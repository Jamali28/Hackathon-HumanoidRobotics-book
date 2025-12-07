# Research & Decisions

This document records the research and decisions made to resolve any "NEEDS CLARIFICATION" items from the `plan.md`.

## Testing Frameworks

### Decision
- **Frontend (Docusaurus/React)**: We will use **Jest** along with **React Testing Library**.
- **Backend (Python/FastAPI)**: We will use **Pytest**.

### Rationale
These selections represent the industry-standard, well-documented, and widely-supported testing frameworks for the chosen technology stack. 
- **Jest** is the de facto standard for testing React applications, and it is officially supported by Docusaurus. **React Testing Library** provides lightweight, user-centric testing utilities that encourage good testing practices.
- **Pytest** is the most popular testing framework for Python, known for its simplicity, powerful features (like fixtures), and excellent integration with libraries like FastAPI.

### Alternatives Considered
- **Frontend**: 
  - `Mocha` & `Chai`: A viable alternative, but Jest offers a more integrated "all-in-one" experience that is common in the React ecosystem.
  - `Cypress`: Better suited for end-to-end (E2E) testing rather than the unit and integration testing we are focused on at this stage. It can be added later if E2E tests are needed.
- **Backend**:
  - `unittest`: Python's built-in testing library. `Pytest` is generally considered more modern, easier to use, and has a richer ecosystem of plugins.
