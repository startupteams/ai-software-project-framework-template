# Feature Roadmap

This file is the project's **ordered strategic implementation plan**. It answers: **what should happen next, and in what sequence, to reach the product's larger goals?**

A roadmap entry is **planning, not approval**. Approval remains in `REQUIREMENTS.md`. Unapproved ideas and deferred work remain in `FUTURE_WORK.md`. The currently executing slice remains in `SPRINT.md`.

## Roadmap rules

- Keep large product goals visible as phases or outcomes, not as an unstructured task list.
- Order phases deliberately. Earlier phases should unlock or de-risk later phases.
- Link each phase to durable IDs from `REQUIREMENTS.md` and/or `FUTURE_WORK.md`; do not duplicate the detailed backlog text here.
- Give every phase a measurable exit gate so agents know when sequencing may advance.
- Record dependencies, blockers, and cross-repository ownership when they affect order.
- Prefer relative sequence (`P0`, `P1`, `P2`) over invented calendar promises. Add dates only when a human has actually chosen them.
- A future-work item may exist without being on the roadmap. Putting it on the roadmap means it is strategically prioritized, **not approved for implementation**.
- Approved requirements may appear on a future roadmap phase before entering the active sprint.
- When priorities change, reorder this file and preserve the reason in Git/ADR/decision records as appropriate.
- Do not turn this file into a second backlog, sprint board, or requirements database.

## Direction

<Describe the durable product outcome or big-picture direction in a few sentences.>

## Ordered phases

| Phase | Goal / outcome | Status | Linked IDs | Dependencies | Exit gate |
|---|---|---|---|---|---|
| P0 | <First enabling outcome> | Planned | `REQ-___`, `FW-___` | <dependency or none> | <measurable proof> |
| P1 | <Next outcome> | Planned | `FW-___` | P0 | <measurable proof> |
| P2 | <Later outcome> | Planned | `FW-___` | P1 | <measurable proof> |

## Sequencing notes

- <Why this order?>
- <What may run in parallel?>
- <What explicitly must not start before an earlier gate?>

## Cross-repository dependencies

| Repository / owner | Needed capability | Phase | Tracking IDs |
|---|---|---|---|
| <repo or team> | <dependency> | P_ | <durable IDs> |

## Roadmap review

Review this roadmap when:
- a phase exit gate is met;
- a major requirement, ADR, dependency, risk, or product goal changes;
- future work is promoted into strategic priority;
- a sprint completes and the next slice must be chosen.

At review, reconcile all four planning layers:

`FUTURE_WORK.md` (inventory) → `FEATURE_ROADMAP.md` (priority/order) → `REQUIREMENTS.md` (approved scope) → `SPRINT.md` (active execution).

Do not infer approval from this file.
