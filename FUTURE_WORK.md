# Future Work

This file is the **canonical repository backlog** for unapproved ideas, defects, deferred scope, follow-ups, enhancements, and possible future requirements.

Items here are not commitments and must not be implemented merely because they are documented. Human approval is required before an item becomes project scope. This file intentionally does **not** prioritize the backlog; strategic priority and sequence belong in `FEATURE_ROADMAP.md`.

## Canonical backlog policy

- Record backlog work here with a stable `FW-###` ID.
- Do not create GitHub Issues, Forgejo Issues, or another external issue solely to track the same backlog item unless a human explicitly requests it.
- When migrating an existing external issue, copy the actionable content into an `FW-###` item, preserve the original issue URL under **Source**, then close the external issue with a migration note.
- Technical debt that is intentionally accepted still gets a TDR. If remediation is deferred, link the TDR from a future-work item instead of creating a duplicate external issue.
- Pull requests, roadmap priority, approved requirements, and sprint execution remain separate records; this policy removes duplicate backlog databases, not review or approval controls.
- When a backlog item becomes strategically important, reference its `FW-###` from `FEATURE_ROADMAP.md` rather than copying its full description. Roadmap placement is priority, not approval.
- See [TDR-0001](docs/tdr/0001-future-work-and-issue-trackers-duplicate-backlog.md) for the portability trade-off and the unresolved long-term question of whether external issue trackers should later become part of a deterministic promotion flow.

When an item is approved:

1. Convert it into one or more `REQ-###` entries in `REQUIREMENTS.md`.
2. Add the approved requirement IDs to an appropriate sprint.
3. Remove the future-work item or mark it as promoted, preserving history in Git.
4. Do not create an external issue unless the human-approved workflow explicitly requires one.

## Show future work in the UI ("Coming soon")

When a project has a user interface, an item here that users would see (a page, setting or panel) is drafted in the UI as a placeholder, so people can point at it in the prototype and say "build this":

- Show it as plain text labelled `Coming soon · FW-###` with the item's ID and status.
- It does nothing: no button, no fake data, no calls. People ask for it by naming the ID.
- Technical debt records are shown the same way, as text with their `TDR-####` ID and status.
- Keep the placeholders as data in one place in the code, so building an item means deleting its entry. A Roadmap page that lists every FW and TDR from these files is a good default.

A placeholder is not approval. Building the real feature still needs a `REQ-###` (steps above).

## FW-001 - Hierarchical context budgets and on-demand instructions

**Idea**

Keep always-loaded agent instructions limited to behavior-changing repository rules, safety boundaries, source-of-truth files and exact validation commands. Move long history, examples, hardware notes and domain SOPs into scoped documents/skills that an agent loads only when the task needs them.

Subagent delegation is an isolation tool, not automatically a cost optimization: record total parent + child usage and prefer delegation for long, narrow investigations whose result can be returned as a small structured evidence summary.

**Why it may matter**

Agent context is a scarce execution resource. Large universal instruction payloads are repeatedly paid for and can dilute the rules that actually matter.

**Notes / dependencies**

- Security/approval guardrails stay always-on.
- A consuming project may define its own tighter instructions.
- Context manifests should distinguish required and optional context.
- Do not optimize only the parent session's token counter.

---

## FW-002 - Verification proof bundle for agent-authored changes

**Idea**

Define a portable proof-bundle contract that a coding agent or CI job can attach to a candidate commit/PR: exact commit/base SHAs, commands/test-profile version, pass/fail/skip results, artifact hashes, runtime/container identity, timestamps, and independent reviewer identity where policy requires it.

The bundle is evidence for review; protected-branch policy still decides which checks must independently run before merge.

**Why it may matter**

As agents produce more branches and commits, the bottleneck moves from typing code to deciding what evidence is trustworthy. A common proof contract lets local iteration stay fast without weakening final gates.

**Notes / dependencies**

- Never accept a model's prose claim that tests passed as proof.
- Expensive full-suite checks may be delayed to coherent PR candidates only where the repository's approved policy permits.
- Required merge checks remain authoritative.

---

## FW-003 - Dependency-install policy hook for agent and CI templates

**Idea**

Give generated project templates an explicit policy surface for dependency installation. Agents and CI should prefer lockfiles/frozen dependency sets and route new dependency requests through a bounded check for age/cooldown, advisories, integrity/attestation changes, install scripts and an auditable exception.

**Why it may matter**

Installing a dependency is code execution, and unattended agents/runners can install attacker-controlled packages before application-level checks run.

**Notes / dependencies**

- This is a framework contract, not a requirement to buy a package-firewall product.
- Concrete registry/proxy implementation belongs to the deployment/security owner.
- Privileged production guests should not allow arbitrary package installation by default.

---

## FW-004 - Governed tool and dependency selection

**Idea**

Coding agents can choose different dependencies for the same job based on model priors, web-search behavior, repository language and surrounding context. The framework should therefore make dependency selection explicit rather than treating an agent recommendation as architecture truth.

**Candidate framework control**

Add an approved technology/dependency catalog with:
- use case/category;
- approved/preferred options;
- license;
- security/support notes;
- known-good version policy;
- reason for preference;
- exception/ADR path.

When a needed dependency is not in the catalog, the agent researches candidates and proposes the architecture-significant choice through the existing ADR process. CI should continue scanning licenses/secrets/vulnerabilities where applicable.

**Evaluation**

Run the same dependency-selection prompts across representative local/cloud coding models and several repository languages. Record variance and whether the framework policy prevents accidental stack drift.

---

<!--
Agents may add useful discoveries here, but may not promote them into approved requirements without human approval.
-->
