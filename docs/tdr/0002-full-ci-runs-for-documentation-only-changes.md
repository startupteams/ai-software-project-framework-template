# TDR-0002: Full CI runs for documentation-only changes

**Status:** Accepted

## Description

Many repositories trigger the complete CI suite for every pull request even when the diff changes only Markdown documentation. Documentation-only changes therefore install application dependencies, run unit/integration tests, start databases, build release artifacts, perform runtime/config checks, and consume hosted/self-hosted runner capacity without exercising changed executable behavior.

This is accepted technical debt while repositories are migrated to change-aware CI.

The standard remediation is **not** to skip the entire required workflow with a top-level path filter. A required workflow that never starts can leave a pull request waiting forever for a check that will never report. Instead, the workflow should always start, classify the changed files, perform lightweight documentation validation, and skip expensive jobs when every changed file is Markdown.

## Impact

- Wasted CI minutes, compute, network bandwidth, dependency downloads, and runner capacity.
- Slower feedback for documentation/process changes.
- More contention with CI that protects executable changes.
- Unnecessary database/service startup and artifact generation.
- Agents may interpret long-running CI as evidence that documentation changes require full runtime validation.

## Possible Solutions

- **Adopted standard:** keep the CI workflow active for every PR; add a small classifier job; if all changed files are `.md` or `.mdx`, run only lightweight text/security validation and skip heavy build/test/dependency/database jobs.
- Keep full CI for any non-Markdown change, including workflow YAML, configuration, scripts, schemas, source, tests, lockfiles, generated runtime assets, and deployment files.
- Preserve existing required-check names where practical. Skipped heavy jobs remain visible rather than making the whole required workflow disappear.
- Do not use workflow-level `paths-ignore` for the required CI workflow unless branch-protection behavior has been explicitly verified.
- Longer term, centralize this classification pattern in reusable CI tooling after the rollout proves stable.

## Owner

Engineering process owner. Repositories should adopt the standard as their existing PR queues permit.
