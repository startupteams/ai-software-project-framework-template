# Requirements

This file is the source of truth for **approved product scope**.

Keep requirements simple, atomic, testable, and implementation-neutral unless implementation detail is itself an approved constraint. Acceptance criteria live with the requirement. Executable tests live with the code and should be linked from the requirement when useful.

There is no system/software requirement split and no separate Markdown test-case hierarchy.

## Rules

- Use stable IDs: `REQ-001`, `REQ-002`, ...
- Group requirements by product feature.
- One requirement should express one capability or constraint.
- Prefer clear mandatory language such as "shall" when it improves precision.
- Acceptance criteria must be observable or verifiable.
- Do not add unapproved future scope here; capture it in `FUTURE_WORK.md`.
- If a requirement changes materially, human approval is required through the normal review process.
- Link ADRs when a requirement depends on a significant approved decision.
- Link tests in **Verification** once the test location exists.

---

## Feature: <Feature Name>

### REQ-001 - <Short requirement title>

**Requirement**

<The product shall ...>

**Acceptance criteria**

- <Observable criterion 1>
- <Observable criterion 2>

**Verification**

- <Automated test path, test name, validation command, or manual verification when necessary>

**Related**

- Future work / PR: <FW-ID or link if applicable>
- ADR/TDR: <link if applicable>

---

<!--
Copy the requirement block above for additional requirements.
Delete this instructional comment as the real requirements are populated.
-->
