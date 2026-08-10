# VPT — Vantage Point Title Creation

Real-estate title creation / title-insurance workflow. Work here is primarily
document and operations work — preparing, reviewing, and producing title
commitments, policies, and related deal documents.

## Claude Code setup

This repository is set up to be worked with Claude Code. Project conventions live
in [`CLAUDE.md`](CLAUDE.md), and the Claude Code tooling incorporated into the repo
is reviewed in
[`docs/claude-code-integration-review.md`](docs/claude-code-integration-review.md).

**Wired into the repo:**

- **Task Observer** skill (`.claude/skills/task-observer/`) — turns repeatable
  work into reusable skills.
- **claude-mem** plugin — persistent memory across sessions. Run
  `npx claude-mem install` once per machine to activate it.
- **claude-code-setup** plugin — Anthropic's official automation recommender.

**Documented for optional machine-level use** (not committed as active config):
OmniRoute (AI gateway routing) and headroom (context compression). See the
integration review for setup steps and the confidentiality considerations that
apply to client data.
