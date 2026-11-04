# TDR-0001: Future Work and issue trackers duplicate the backlog

**Status:** Accepted

## Description

The framework currently allows the same follow-up work to be recorded in both `FUTURE_WORK.md` and an external issue tracker such as GitHub Issues or Forgejo Issues. AI agents have been using both paths without one consistent rule. The two backlogs drift, duplicate each other, and work can be lost because an agent or human must remember which system contains the authoritative record.

For now, `FUTURE_WORK.md` is the canonical backlog for unapproved ideas, defects, deferred work, follow-ups, and other work not yet promoted into approved requirements/sprint scope. Agents should not create GitHub or Forgejo issues for those items unless a human explicitly asks for an external issue.

This is intentionally a portable default: the backlog stays in the codebase, travels with Git history, works with GitHub, Forgejo, or another Git host, and does not require issue-format migration when hosting changes.

The remaining debt is that GitHub and Forgejo issue trackers exist for valid workflow reasons, and the framework has not yet decided whether to abandon them for backlog tracking permanently or use a deterministic synchronization/promotion process.

## Impact

- Existing repositories may contain open issues that duplicate or conflict with `FUTURE_WORK.md`.
- Agents may still follow older repository instructions that require issue IDs in branch names, commits, or PRs.
- GitHub/Forgejo issue-specific features such as assignments, labels, milestones, notifications, and board views are not the canonical backlog while this debt is active.
- Without a migration sweep, historical issues remain easy to miss.
- A future decision may require either removing `FUTURE_WORK.md` in favor of issue trackers or defining a one-way conversion/synchronization process.

## Possible Solutions

- **Current direction:** keep `FUTURE_WORK.md` as the sole canonical backlog. Sweep active repositories, migrate actionable open issues into stable `FW-###` entries with source links, close migrated issues, and update agent/Git instructions so new issues are not created by default.
- Later, if external issue trackers provide enough value, define one deterministic direction only, for example `FUTURE_WORK.md -> external issue` when work is approved for execution. The Markdown record remains canonical until that explicit policy changes.
- Alternatively, replace `FUTURE_WORK.md` with external issues only, but do so through a human-approved migration plan that preserves portability and history.

## Owner

Engineering process owner. Human review is required before changing the canonical backlog policy.
