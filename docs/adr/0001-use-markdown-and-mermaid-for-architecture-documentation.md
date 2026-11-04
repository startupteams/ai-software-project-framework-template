# ADR-0001: Use Markdown and Mermaid for Architecture Documentation

**Status:** Accepted  
**Date:** 2026-09-25

## Context

The project framework is primarily used by AI agents and humans creating software products at high iteration speed. The documentation format should be easy to read in source form, easy to edit with agents, easy to diff in Git, and should avoid a separate documentation build toolchain unless a project later proves it needs one.

The source arc42/C4 example uses AsciiDoc, docToolchain, Structurizr DSL, and generated documentation. The project owner explicitly chose to remain entirely Markdown and delegated the initial Mermaid-versus-Structurizr choice for the starter framework.

## Decision

Use Markdown for repository documentation and Mermaid as the default architecture diagram format.

Use the arc42 section structure in a single `docs/ARCHITECTURE.md` file and use C4 concepts inside the relevant sections when diagrams are useful.

A project may later adopt Structurizr DSL or another architecture-modeling tool if its complexity justifies the added tooling. That change requires a human-approved ADR.

## Consequences

- Documentation is readable and editable directly in the repository without a separate documentation build system.
- Agents can update text and diagrams using one Markdown-native workflow.
- Git diffs remain straightforward.
- Mermaid provides less formal C4 modeling semantics than Structurizr DSL.
- Very large or highly regulated architecture models may eventually benefit from migration to a dedicated modeling tool.

## References

- arc42: <https://arc42.org/>
- C4 Model: <https://c4model.com/>
- arc42 + C4 example: <https://github.com/bitsmuggler/arc42-c4-software-architecture-documentation-example>
