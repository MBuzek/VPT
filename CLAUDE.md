# VPT — Vantage Point Title Creation

VPT is a **real-estate title creation / title-insurance workflow**. Work in this
repository is primarily document and operations work — preparing, reviewing, and
producing title commitments, policies, and related deal documents — not building
software. Optimize for accuracy, traceability, and repeatable process.

## Working conventions

- Treat title/deal documents as the source of truth. When a document and a note
  disagree, surface the discrepancy rather than silently picking one.
- Never commit client PII, deal-identifying details, or credentials. `.env`,
  `.env.*`, and `secrets/**` are read-denied in `.claude/settings.json` — keep
  sensitive material out of the repo.
- Prefer capturing a repeatable procedure as a reusable skill over re-explaining
  it each session (see Task Observer below).

## Claude Code tooling incorporated into this repo

This repo is wired up with the integrations reviewed in
[`docs/claude-code-integration-review.md`](docs/claude-code-integration-review.md).
Read that document for the full rationale, install steps, and which tools are
repo-level vs. machine-level.

- **Task Observer** (`.claude/skills/task-observer/`) — vendored skill that
  watches sessions for repeatable workflows worth turning into skills.
- **claude-mem** — plugin (enabled in `.claude/settings.json`) for persistent
  memory across sessions. Requires a one-time `npx claude-mem install` on the
  machine before its hooks work.
- **claude-code-setup** — Anthropic official skill/plugin for recommending
  further automations tailored to this repo.
- **OmniRoute** and **headroom** — machine-level tools; documented in the review,
  not wired into committed settings (see the review for why).

## Task Observer activation (required for reliable triggering)

At the **start of every task-oriented session** in this repo — before using tools
to produce deliverables — invoke the **task-observer** skill
(`.claude/skills/task-observer/SKILL.md`). Its own guidance notes that
description-level matching alone is not enforceable, so this instruction is the
enforcement. Keep observations generalizable and strip any client-identifying
detail before recording them.
