# TDR-0003: GitHub Actions minutes are billed per job and per duplicate run

**Status:** Accepted

## Description

GitHub bills private-repository Actions per job, each rounded up to a whole minute. In practice most wasted minutes come from workflow patterns, not from any single slow test:

- **One minute per job, however short.** A workflow with a classifier plus N parallel jobs of 5-30 seconds bills N+1 minutes for well under 2 minutes of work.
- **Push-to-`main` re-runs.** CI runs on the pull request and again on the merge push, re-testing the same tree.
- **Feature-branch push triggers** next to `pull_request`, so every push runs twice.
- **Tests that wait on real network services**, timing out on every call instead of failing fast.
- **The same suite twice** (for example two database dialects where one is a strict subset), and **audits on every PR** whose inputs did not change.
- **Automation pushes** (scheduled data or ledger updates) running the full suite for data-only changes.

Scheduled and deploy workflows on a self-hosted runner do not consume hosted minutes.

## Standard (adopted)

Extends [TDR-0002](0002-full-ci-runs-for-documentation-only-changes.md) and `docs/CI_VALIDATION_POLICY.md`:

1. **One job per CI workflow.** The classifier is the first step of that job; later steps carry `if: steps.scope.outputs.full_ci == 'true'`. Service containers (for example Postgres) attach to the one job; use separate databases when two steps need a clean schema.
2. **`pull_request` (+ `workflow_dispatch`) only on GitHub.** No `push: main`, no feature-branch `push`. A repo whose workflow also runs on a self-hosted forge may keep `push: main` with the job guarded by `if: github.event_name != 'push' || github.server_url != 'https://github.com'`.
3. **`concurrency`** with `cancel-in-progress: true`, grouped by PR number.
4. **`timeout-minutes`** on every job (15-20).
5. **Input-gated checks.** Dependency audits run when the lock/freeze file changes (and on a manual run); config checks run when that config changes; data-only PRs run the data validator, not the app suite, where the repo has one.
6. **No test reaches the local network or the internet.** Point clients at a refusing loopback port (for example `https://127.0.0.1:9`) in test setup; a test that waits for a timeout is a bug.
7. **One suite per dialect that matters.** Run the production database dialect; drop a second run that is a strict subset.
8. **Markdown-only PRs** keep the TDR-0002 lightweight check (about 1 billed minute); top-level `paths-ignore` is still not used.
9. **Markdown that tests read is not Markdown-only.** Where a test reads `FUTURE_WORK.md`, `REQUIREMENTS.md` or `docs/tdr/` (the "Coming soon" roadmap pattern), the classifier treats those files as full CI. Otherwise a docs-only PR that adds an FW item can skip the roadmap test and turn `main` red.

## Impact

- Large reductions in billable minutes are typical (often 3x or more) once these patterns are removed.
- Check names change to one `ci`/`CI` job per workflow; update branch protection if it pins the old names.
- A PR merged while behind `main` is not re-tested on `main`; `workflow_dispatch` runs CI on demand.
- A new upstream CVE in an unchanged lock file is found on the next lock change or manual run, not on every PR.

## Possible Solutions (follow-ups)

- A shared reusable workflow for the classifier step, so every repository uses one copy.
- A weekly scheduled dependency audit on a self-hosted runner instead of per-PR audits.
- Move heavy suites to self-hosted runners.

## Owner

Engineering process owner. Repository owners adopt it when they next touch CI.
