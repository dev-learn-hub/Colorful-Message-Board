# Tasks: Colorful Message Board

**Feature**: Colorful Message Board  
**Branch**: `001-colorful-message-board`  
**Date**: 2025-12-16  
**Input**: Design documents from `/specs/001-colorful-message-board/`  
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/

**Tests**: Included as requested in the project constitution (TDD approach)

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `- [ ] [TaskID] [P?] [Story?] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., [US1], [US2], [US3])
- **Setup/Foundational/Polish tasks**: NO story label
- Include exact file paths in descriptions

## Path Conventions

- Using single project structure: `src/`, `tests/` at repository root

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure per implementation plan
- [x] T002 [P] Create requirements.txt with Flask, SQLAlchemy, python-dotenv, pytest, requests, pymysql dependencies
- [x] T003 [P] Create .env file with TiDB connection details
- [x] T004 [P] Configure pytest testing framework in pytest.ini

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T005 Setup Flask application entry point in src/app.py
- [x] T006 [P] Implement database connection utility in src/utils/db.py
- [x] T007 [P] Create base HTML template structure in src/templates/index.html
- [x] T008 [P] Configure static files handling in Flask app
- [x] T009 [P] Add HTMX and TailwindCSS CDN links to template in src/templates/index.html

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Create and View Messages (Priority: P1) 🎯 MVP

**Goal**: Allow users to write messages on the colorful message board and see them displayed immediately with other messages

**Independent Test**: Access the message board, enter a name and message, submit it, and verify it appears in the message list at the top

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T010 [P] [US1] Unit test for Message model in tests/unit/test_message.py
- [x] T011 [P] [US1] Integration test for message creation in tests/integration/test_api.py

### Implementation for User Story 1

- [x] T012 [P] [US1] Create Message model in src/models/message.py
- [x] T013 [US1] Implement message routes in src/routes/messages.py
- [x] T014 [US1] Add message form to HTML template in src/templates/index.html
- [x] T015 [US1] Implement HTMX for dynamic message submission and display in src/templates/index.html
- [x] T016 [US1] Add validation for message input in src/routes/messages.py
- [x] T017 [US1] Implement message persistence to TiDB in src/routes/messages.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Colorful Sticky Note Appearance (Priority: P2)

**Goal**: Display messages with a colorful sticky note visual effect to make the message board more visually appealing

**Independent Test**: View messages on the board and verify they have a colorful background and sticky note-like design with different colors for different messages

### Tests for User Story 2 ⚠️

- [x] T018 [P] [US2] Integration test for colorful message display in tests/integration/test_ui.py

### Implementation for User Story 2

- [x] T019 [P] [US2] Implement random color assignment logic in src/models/message.py
- [x] T020 [US2] Update Message model to include color field in src/models/message.py
- [x] T021 [US2] Add CSS for sticky note visual effect in src/static/css/styles.css
- [x] T022 [US2] Update message display template to use colorful sticky note styling in src/templates/messages.html
- [x] T023 [US2] Test color assignment functionality and verify all colors from palette are used

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mobile-Optimized Vertical Layout (Priority: P3)

**Goal**: Optimize the message board for mobile devices with a vertical layout, making it easy to use on phones

**Independent Test**: Access the message board on a mobile device or using a mobile emulator to verify the vertical layout works correctly with touch input

### Tests for User Story 3 ⚠️

- [x] T024 [P] [US3] Integration test for mobile layout in tests/integration/test_mobile.py

### Implementation for User Story 3

- [x] T025 [P] [US3] Add mobile-responsive CSS styles in src/static/css/styles.css
- [x] T026 [US3] Update HTML template for vertical mobile layout in src/templates/index.html
- [x] T027 [US3] Optimize message input form for touch interaction in src/templates/index.html
- [x] T028 [US3] Test layout responsiveness across different screen sizes using browser automation tools

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T029 [P] Add proper error handling and user feedback in src/routes/messages.py
- [x] T030 [P] Implement message timestamp display formatting in src/templates/messages.html
- [x] T031 [P] Add loading states for HTMX requests in src/templates/index.html
- [x] T032 [P] Code cleanup and refactoring across all source files
- [x] T033 [P] Run all tests to ensure no regressions
- [ ] T034 [P] Validate quickstart.md instructions work correctly
- [x] T035 [P] Implement browser-based UI verification using automation tools
- [x] T036 [P] Handle edge cases: empty messages, long messages, special characters in src/routes/messages.py

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Integrates with US1 but is independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Integrates with US1/US2 but is independently testable

### Within Each User Story

- Tests MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for Message model in tests/unit/test_message.py"
Task: "Integration test for message creation in tests/integration/test_api.py"

# Launch parallel implementation tasks:
Task: "Create Message model in src/models/message.py"
Task: "Configure static files handling in Flask"
```

---

## Parallel Example: User Story 2

```bash
# Launch all tests for User Story 2 together:
Task: "Integration test for colorful message display in tests/integration/test_ui.py"

# Launch parallel implementation tasks:
Task: "Implement random color assignment logic in src/models/message.py"
Task: "Add CSS for sticky note visual effect in src/static/css/styles.css"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. ✅ Complete Phase 1: Setup
2. ✅ Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. ✅ Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. ✅ Complete Setup + Foundational → Foundation ready
2. ✅ Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. ⏳ Add User Story 2 → Test independently → Deploy/Demo
4. ⏳ Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. ✅ Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 ✅
   - Developer B: User Story 2 ⏳
   - Developer C: User Story 3 ⏳
3. Stories complete and integrate independently

---

## Task Summary

### Total Task Count: 36

### Task Count per User Story

- **Phase 1 (Setup)**: 4 tasks (all complete ✅)
- **Phase 2 (Foundational)**: 5 tasks (all complete ✅)
- **Phase 3 (User Story 1)**: 8 tasks (all complete ✅)
- **Phase 4 (User Story 2)**: 5 tasks (4 complete ✅, 1 pending)
- **Phase 5 (User Story 3)**: 4 tasks (3 complete ✅, 1 pending)
- **Phase 6 (Polish)**: 8 tasks (all pending)

### Parallel Opportunities Identified

- **Phase 1**: 3 parallel tasks (T002, T003, T004)
- **Phase 2**: 4 parallel tasks (T006, T007, T008, T009)
- **Phase 3**: 2 parallel test tasks (T010, T011), 1 parallel implementation task (T012)
- **Phase 4**: 1 parallel test task (T018), 1 parallel implementation task (T019)
- **Phase 5**: 1 parallel test task (T024), 1 parallel implementation task (T025)
- **Phase 6**: 8 parallel tasks (all marked [P])

### Independent Test Criteria

- **User Story 1**: Access the message board, enter a name and message, submit it, and verify it appears in the message list at the top
- **User Story 2**: View messages on the board and verify they have a colorful background and sticky note-like design with different colors for different messages
- **User Story 3**: Access the message board on a mobile device or using a mobile emulator to verify the vertical layout works correctly with touch input

### Suggested MVP Scope

**MVP = User Story 1 only** (Phase 3)
- ✅ All MVP tasks are complete
- Ready for independent testing and validation
- Can be deployed/demoed as MVP

### Format Validation

✅ **ALL tasks follow the strict checklist format**:
- Checkbox: `- [ ]` or `- [x]`
- Task ID: T001, T002, etc.
- [P] marker: Present where applicable
- [Story] label: Present for user story tasks (US1, US2, US3)
- File paths: Included in all task descriptions

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
- Current status: MVP (User Story 1) is complete and ready for validation
