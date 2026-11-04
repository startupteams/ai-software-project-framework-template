# Architecture

This is the project's single, lean architecture document. It follows the arc42 section structure and uses C4 concepts where diagrams improve understanding.

Keep it current with the code. Prefer concise facts, links, and diagrams over speculative prose. If a section is not yet useful, write `Not yet applicable` rather than inventing detail.

Default diagrams use **Mermaid** so architecture remains Markdown-native, diffable, and readable without an additional documentation toolchain.

## 1. Introduction and Goals

### Purpose

<What product/system are we building and why?>

### Requirements Overview

Summarize only the architecturally significant requirements. Link to `../REQUIREMENTS.md` rather than duplicating the full requirement set.

- `<REQ-ID>` - <short architectural relevance>

### Quality Goals

List the few quality attributes that most strongly shape the architecture, preferably with measurable targets and requirement IDs.

### Stakeholders

| Stakeholder / Role | Primary Concern |
|---|---|
| <role> | <expectation or concern> |

## 2. Architecture Constraints

Record fixed constraints that materially limit the solution space, such as compliance, hosting, integration, budget, device/runtime, data residency, or compatibility constraints.

- <constraint>

Do not treat a preference as a constraint unless a human has approved it as one.

## 3. Context and Scope

### Business Context / C4 System Context

Describe users and external systems that interact with this product.

<!-- Add a Mermaid flowchart here when a diagram improves understanding. -->

### Technical Context

Document external interfaces, protocols, data flows, upstream/downstream dependencies, and trust boundaries that matter architecturally.

## 4. Solution Strategy

Summarize the small number of decisions that define the overall approach: major decomposition, architectural style, key technology strategy, data strategy, deployment strategy, and how the quality goals will be achieved.

Link significant choices to ADRs instead of duplicating their rationale.

## 5. Building Block View

Describe the major logical or deployable building blocks and their responsibilities.

Use C4-style levels only as far as they add value:

- **Level 2 / Containers:** applications, services, data stores, workers, clients, etc.
- **Level 3 / Components:** only for complex containers where component boundaries help agents/humans reason about the code.

<!-- Mermaid diagrams are preferred by default. Keep diagram nodes aligned with real code/deployment boundaries. -->

| Building Block | Responsibility | Interfaces / Dependencies | Code Location |
|---|---|---|---|
| <name> | <purpose> | <important interfaces> | <path when known> |

## 6. Runtime View

Document important runtime scenarios that are difficult to infer from static structure, such as authentication, critical transactions, background processing, failure/retry behavior, or multi-service workflows.

Use Mermaid sequence diagrams when useful.

### <Runtime Scenario>

<Describe the trigger, major interactions, success path, and important failure behavior.>

## 7. Deployment View

Describe where the software runs and how deployable building blocks map to infrastructure.

Include environments, networks/trust zones, persistent data, external managed services, scaling model, and relevant operational constraints.

Do not assume Docker, Kubernetes, cloud provider, or another deployment platform until the project has selected it.

## 8. Cross-Cutting Concepts

Document concepts that affect many parts of the system, for example:

- authentication / authorization;
- error handling;
- configuration and secrets;
- data validation;
- logging / tracing / metrics;
- privacy and security;
- resilience, retries, idempotency;
- internationalization;
- caching;
- testing strategy.

Only include concepts that are actually relevant.

## 9. Architecture Decisions

Significant decisions are stored as ADRs in `adr/`.

- [ADR-0001 - Use Markdown and Mermaid for architecture documentation](adr/0001-use-markdown-and-mermaid-for-architecture-documentation.md)

Agents may draft ADRs, but agent-originated significant decisions remain `Proposed` until human approval. Human-directed decisions may be recorded as `Accepted` and must be surfaced in review.

## 10. Quality Requirements

Reference measurable quality requirements from `../REQUIREMENTS.md` rather than creating a second requirements database.

| Requirement | Quality Attribute | Target / Scenario | Verification |
|---|---|---|---|
| <REQ-ID> | <e.g. performance> | <measurable target> | <test/measurement> |

## 11. Risks and Technical Debt

### Risks

Maintain a concise prioritized list of current architectural/technical risks that are not necessarily accepted debt.

| Risk | Impact | Mitigation / Next Step |
|---|---|---|
| <risk> | <impact> | <mitigation> |

### Technical Debt

Accepted technical debt is stored as TDRs in `tdr/` so it has an owner and can be reviewed later.

- [TDR-0001 - Future Work and issue trackers duplicate the backlog](tdr/0001-future-work-and-issue-trackers-duplicate-backlog.md)
- [TDR-0002 - Full CI runs for documentation-only changes](tdr/0002-full-ci-runs-for-documentation-only-changes.md)
- [TDR-0003 - GitHub Actions minutes are billed per job and per duplicate run](tdr/0003-github-actions-minutes-billed-per-job.md)

## 12. Glossary

| Term | Definition |
|---|---|
| <term> | <project-specific meaning> |
