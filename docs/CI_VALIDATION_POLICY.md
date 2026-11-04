# CI Validation Policy

CI should be proportional to the files that changed.

## Documentation-only pull requests

When every changed file is Markdown (`.md` or `.mdx`):

- keep the required CI workflow running so GitHub/Forgejo receives a result;
- run one lightweight validation job;
- verify changed documents are readable UTF-8 text;
- reject merge-conflict markers and obvious credential/private-key material;
- skip application dependency installation, unit/integration tests, databases, builds, release artifacts, runtime/config validation, and other expensive executable checks.

Any non-Markdown file makes the change **full CI**.

Markdown that a test reads (for example `FUTURE_WORK.md`, `REQUIREMENTS.md` or `docs/tdr/` behind a roadmap page) also makes the change full CI ([TDR-0003](tdr/0003-github-actions-minutes-billed-per-job.md) rule 9).

Do not implement this by applying a top-level `paths-ignore` to a required workflow unless branch-protection behavior has been explicitly verified. If the required workflow never starts, the pull request can remain stuck waiting for a check that never reports.

## GitHub Actions pattern

Use **one job** (GitHub bills each job rounded up to a whole minute, [TDR-0003](tdr/0003-github-actions-minutes-billed-per-job.md)). Its first step, after a `fetch-depth: 0` checkout, is the classifier: compare the pull request base SHA with `GITHUB_SHA` and export a boolean such as `full_ci`. Every later step uses:

```yaml
if: steps.scope.outputs.full_ci == 'true'
```

The classifier step itself performs the lightweight documentation validation when `full_ci == false`.

Triggers: `pull_request` and `workflow_dispatch` only (no `push: main`, no feature-branch `push`), with:

```yaml
concurrency:
  group: ci-${{ github.event.pull_request.number || github.ref }}
  cancel-in-progress: true
```

and `timeout-minutes` on the job. Audits and config checks run only when their input files change. Tests never reach the local network or the internet.

See [TDR-0002](tdr/0002-full-ci-runs-for-documentation-only-changes.md) and [TDR-0003](tdr/0003-github-actions-minutes-billed-per-job.md).
