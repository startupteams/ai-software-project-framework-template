# Agent Readiness - Level 3 Target

This repository framework targets **production-grade, Level 3-style agent readiness** without prescribing a programming language, framework, CI provider, test framework, container runtime, or deployment platform.

A blank framework cannot literally satisfy build, test, observability, or deployment signals before a product stack exists. The rule is therefore: **select the tools that best fit the product, then satisfy these capability outcomes before treating the repository as production-ready for autonomous execution.**

## Level 3 Readiness Gate

### 1. Style and Validation

- [ ] Formatting conventions are defined where applicable.
- [ ] Lint/static-analysis checks are defined where applicable.
- [ ] Type checking is defined where the selected language/ecosystem benefits from it.
- [ ] The validation commands are documented and quick enough for agents to run frequently.
- [ ] CI validation is proportional: Markdown-only changes use a lightweight always-reporting docs check, while any non-Markdown change runs full project CI.

### 2. Build System

- [ ] Setup/build commands are deterministic and documented.
- [ ] Dependencies and runtime versions are reproducible/pinned appropriately for the selected stack.
- [ ] A fresh checkout can be made runnable using documented steps.
- [ ] Build failures produce actionable diagnostics.

### 3. Testing

- [ ] Automated tests cover core behavior.
- [ ] Integration tests exist where integration risk warrants them.
- [ ] End-to-end tests cover critical user journeys where applicable.
- [ ] Tests can run without unsafe dependence on production systems/data.
- [ ] Flaky tests are treated as defects rather than ignored.

### 4. Documentation and Instructions

- [x] `AGENTS.md` exists with agent operating rules.
- [x] Approved scope and acceptance criteria have a defined home in `REQUIREMENTS.md`.
- [x] Architecture has a defined home in `docs/ARCHITECTURE.md`.
- [ ] Exact setup/run/build/test/validation/deploy commands are documented after tool selection.
- [ ] Troubleshooting information covers recurring non-obvious failures.
- [ ] Documentation is updated in the same change as behavior/architecture changes.

### 5. Development Environment and Execution

- [ ] The selected development environment is reproducible.
- [ ] Agents have an isolated/sandboxed execution path appropriate to the project risk.
- [ ] Required local/external dependencies are documented and reproducible.
- [ ] Long-running agent work can be resumed or handed off without relying on hidden local state.

### 6. Code Quality

- [ ] Code is modular with clear boundaries that agents and humans can reason about.
- [ ] Naming and directory structure are consistent and documented by usage.
- [ ] Complexity is actively controlled; oversized files/functions are refactored when they hinder reasoning or testing.
- [ ] Public/internal interfaces are clear enough to change safely.

### 7. Debugging and Observability

- [ ] Error messages provide actionable context.
- [ ] Structured logging exists where appropriate.
- [ ] Metrics exist for operationally important behavior where applicable.
- [ ] Tracing/correlation exists for distributed or multi-step flows where applicable.
- [ ] Agents/humans have a documented path to inspect failures without exposing secrets.

### 8. Security and Governance

- [ ] Protected branches / equivalent controls prevent unreviewed production merges.
- [ ] GitHub "Automatically delete head branches" is on, so merged PR branches do not pile up.
- [ ] Human approval is required before merge under the current operating model.
- [ ] Secret scanning and dependency/security scanning are configured using tools appropriate to the stack.
- [ ] Secrets are not stored in source control.
- [ ] Security-sensitive boundaries are documented in architecture when applicable.
- [ ] High-risk/destructive actions require explicit human approval.

## Repository-Level Operating Signals

Before calling the project agent-ready for production work, a human should be able to answer **yes** to all of these:

- Can an agent discover what it is supposed to build from approved requirements?
- Can it discover the exact commands needed to set up, validate, test, and build the project?
- Can it run those commands in a reproducible, isolated environment?
- Can it understand the system boundaries and important decisions from repository-local documentation?
- Can it detect failures through tests, diagnostics, logs, and other relevant observability?
- Are security controls and human escalation points explicit?
- Will significant agent-originated decisions be stopped for human approval?
- Can another human or agent continue the work from the repository and handoff alone?

## Future autonomy

The current policy requires human review before merge. A future operating model may allow low-risk changes to pass CI and merge autonomously within explicit guardrails, but that is future work and requires a separate human-approved governance decision before implementation.
