# AGENTS.md

Instructions for autonomous and semi-autonomous coding agents working in this repository.

## 1. Authority model

Humans set product intent, approve scope, approve significant decisions, and approve merges.

Agents may:

- inspect the repository;
- propose a short plan;
- implement approved requirements;
- create or update automated tests;
- update documentation affected by the change;
- add newly discovered ideas, defects, follow-ups, and deferred work to `FUTURE_WORK.md`;
- update `FEATURE_ROADMAP.md` when human-directed priorities or sequencing change, without treating roadmap placement as scope approval;
- draft ADRs and TDRs;
- run non-destructive validation;
- prepare commits and pull requests.

Agents must not:

- silently add product scope;
- promote future work into approved requirements without human approval;
- accept their own newly invented significant architecture decision;
- merge their own work under the current operating model;
- commit directly to `main`/production branches;
- use destructive commands, rotate secrets, alter production data, change permissions, or modify infrastructure without explicit human approval;
- hide failed validation, security concerns, or unresolved trade-offs.

## 2. Read before planning

For every meaningful change, read the relevant parts of:

1. `README.md`
2. `REQUIREMENTS.md`
3. `SPRINT.md`
4. `docs/ARCHITECTURE.md`
5. relevant files in `docs/adr/`
6. relevant files in `docs/tdr/`
7. `FUTURE_WORK.md` when scope or follow-up work is involved

Repository-local instructions and approved requirements are the primary source of truth.

## 3. Requirement discipline

Implementation work should trace to one or more `REQ-###` entries.

Before editing, summarize:

- the requirement IDs being implemented;
- the acceptance criteria;
- the files/components likely to change;
- assumptions or ambiguities;
- the validation that will prove the change works.

If the requested work is not covered by an approved requirement, do one of the following:

- ask for human approval to add/modify the requirement; or
- record the idea in `FUTURE_WORK.md` if it is not part of the current scope.

### Backlog source of truth

`FUTURE_WORK.md` is the canonical backlog. Agents must not create GitHub Issues, Forgejo Issues, or another external issue for ideas, defects, follow-ups, deferred work, or technical-debt remediation unless a human explicitly asks for that external issue.

When an existing external issue is still actionable, migrate its useful content into a stable `FW-###` entry, preserve the source issue URL, then close the issue with a migration note. If the issue is already completed, obsolete, duplicate, or otherwise non-actionable, close it instead of creating future work.

See `docs/tdr/0001-future-work-and-issue-trackers-duplicate-backlog.md`.

If the project has a user interface and the idea is something users would see, also draft it in the UI as a plain-text "Coming soon · FW-###" placeholder with no button (see `FUTURE_WORK.md`). The placeholder does nothing and is not approval to build.

Do not invent scope merely because it seems useful. Do not move an item onto the roadmap unless the human has directed its priority or sequencing, or the task explicitly asks you to maintain the roadmap.

When planning the next work, reconcile the layers in order: `FUTURE_WORK.md` (inventory) → `FEATURE_ROADMAP.md` (priority/order) → `REQUIREMENTS.md` (approved scope) → `SPRINT.md` (active execution).

## 4. Planning and execution

Before meaningful edits, provide a short implementation plan. Keep the plan proportional to the change.

During execution:

- work in a dedicated branch/worktree/sandbox;
- keep the diff focused;
- follow the existing architecture and project conventions;
- prefer readable, conventional code over clever code;
- avoid unrelated cleanup;
- preserve backward compatibility unless an approved requirement or ADR says otherwise;
- update affected documentation in the same change.

If the implementation grows materially beyond the approved plan, stop and surface the scope increase.

## 5. Significant decisions and ADRs

Create or update an ADR when a change makes a significant, durable decision about architecture, major dependencies, data/storage, external integrations, security boundaries, deployment model, scalability approach, or another choice that future maintainers are likely to ask "why did we choose this?"

### Human-directed decision

If a human explicitly made the decision, the agent may record it as `Status: Accepted`. The ADR must still be called out in the pull request so the human sees what was recorded.

### Agent-originated decision

If the agent concludes a significant decision is needed, create a draft ADR with `Status: Proposed` and surface it for human approval. Do not treat it as approved until a human accepts it.

Use `docs/adr/TEMPLATE.md`.

## 6. Technical debt and TDRs

Create a TDR when a change intentionally leaves known technical debt such as a shortcut, workaround, temporary design, missing test, manual step, or deferred reliability/security/performance/maintainability improvement.

Use `docs/tdr/TEMPLATE.md` and keep the record concise.

An agent may propose a TDR, but the human reviewer should confirm that the debt is acceptable and that the owner is appropriate.

## 7. Validation

Use the exact validation commands documented by the project once the implementation stack is selected.

Run all checks relevant to the change, such as:

- formatting;
- lint/static analysis;
- type checking where applicable;
- unit tests;
- integration tests;
- end-to-end tests where applicable;
- build/package validation;
- security/secret/dependency checks;
- deployment or readiness checks when relevant.

Report exactly what passed, failed, or was not run. Never imply that a check passed if it was skipped or unavailable.

If expected commands are not documented, surface that as an agent-readiness gap instead of guessing silently.

### Proportional CI

Documentation-only changes must not consume the full application CI suite by default. When every changed file is Markdown, CI should keep an always-reporting lightweight check for UTF-8/text integrity, conflict markers, and obvious secrets while skipping expensive build/test/dependency/database/runtime jobs. Any non-Markdown change receives full CI. Do not use workflow-level `paths-ignore` for a required CI workflow unless required-check behavior is explicitly verified. See `docs/CI_VALIDATION_POLICY.md` and TDR-0002.

## 8. Security and data handling

- Do not commit secrets, credentials, private keys, access tokens, or sensitive customer/company data.
- Treat generated shell commands, migrations, dependencies, and configuration changes as untrusted until reviewed.
- Do not weaken authentication, authorization, encryption, logging, isolation, or monitoring merely to make a task easier.
- Surface security-sensitive behavior for explicit human review.

## 9. Git and pull requests

- Use a dedicated branch; direct commits to `main`/production branches are prohibited.
- Branch format: `type/work-id-short-description` using the canonical repository ID when one exists (for example, `feat/FW-024-bnpl-checkout` or `fix/REQ-017-session-timeout`).
- Commit format: `type(scope): short description (FW-###)`, `type(scope): short description (REQ-###)`, or another applicable repository-local durable ID such as a TDR/ADR.
- Commit scope is required.
- Do not require or create an external issue ID merely to satisfy Git metadata. Reference an external issue only when a human explicitly chose that tracker for the work.
- Keep commits and PRs small enough to review.
- Required validation must pass before merge.
- A human reviewer must approve before merge under the current operating model.
- Delete a branch after its PR merges (for example, enable your Git host's automatic head-branch deletion). Never delete `main`, a production/release branch, or a branch that is not merged.

Every PR should state:

- feature / requirement / future-work IDs;
- what changed and why;
- files/components changed;
- validation performed and results;
- known risks or limitations;
- documentation changes;
- ADRs/TDRs added or changed;
- future-work items discovered;
- reviewer focus areas.

## 10. Stop and ask for human judgment when

- requirements conflict or are materially ambiguous;
- a new significant ADR decision is required;
- credentials or restricted access are required;
- a destructive action is needed;
- tests fail unexpectedly and the cause is not understood;
- security-sensitive behavior changes;
- production data or infrastructure would be changed;
- the diff grows substantially beyond the planned scope;
- a future-work idea would need to become approved product scope.

## 11. Handoff standard

At the end of a work session or before handing work to another agent/human, provide:

1. requirement IDs addressed;
2. concise summary of changes;
3. files changed;
4. validation commands and results;
5. known risks / unresolved questions;
6. ADR/TDR status;
7. future-work items discovered;
8. recommended next action.
