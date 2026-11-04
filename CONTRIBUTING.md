# Contributing

Thanks for helping improve the AI-First Software Project Framework. This repository is a template, so changes should make it more useful for *any* project, language, agent, or Git host.

## How to propose a change

1. **Small fixes** (typos, broken links, clearer wording): open a pull request directly.
2. **New ideas or larger changes**: add an `FW-###` entry to [`FUTURE_WORK.md`](FUTURE_WORK.md) in a pull request, or open a discussion, before writing the full change.
3. **Decisions that change how the framework works**: include an ADR in `docs/adr/` (copy `TEMPLATE.md`) with `Status: Proposed`. A maintainer accepts it during review.
4. **Known shortcuts**: if your change leaves deliberate debt, add a TDR in `docs/tdr/`.

## Guidelines

- Stay tool-neutral. Do not require a specific language, CI provider, agent, or hosting platform.
- Keep it lean. Prefer one clear rule over a long explanation.
- Keep diagrams in Mermaid and documents in Markdown (ADR-0001).
- Use [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): short description`.
- Update every file affected by your change in the same pull request, and fill in the pull request template.

## Validation

CI runs `python3 .github/scripts/check_docs.py`. Run it locally before opening a pull request. It checks that Markdown files are valid UTF-8, contain no merge-conflict markers or private-key material, and that relative links point to files that exist.

## License

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE).
