# Repository Integration Review — Claude Code tooling for VPT

**Repository:** `MBuzek/VPT` (Vantage Point Title Creation)
**Context:** VPT is a real-estate title creation / title-insurance workflow. The
goal of "incorporating" the five projects below is to make Claude Code a reliable
assistant for **document and operations work** — preparing and reviewing title
commitments, policies, and deal documents — with continuity across sessions and a
growing library of repeatable procedures.
**Date:** 2026-08-10

---

## TL;DR

Five projects were requested. They live at two different levels, and that
distinction drives what could actually be committed to this repo:

| Project | What it is | Level | Decision for VPT |
|---|---|---|---|
| [one-skill-to-rule-them-all](https://github.com/rebelytics/one-skill-to-rule-them-all) (Task Observer) | Meta-skill that turns real work into reusable skills | Repo-level skill | **Wired up** — vendored into `.claude/skills/task-observer/` |
| [claude-mem](https://github.com/thedotmack/claude-mem) | Persistent cross-session memory | Claude Code plugin | **Wired up** — enabled in `.claude/settings.json` (one-time machine install required) |
| [claude-code-setup](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup) | Anthropic official skill that recommends automations for a repo | Plugin/skill | **Wired up** — enabled from the official marketplace |
| [OmniRoute](https://github.com/diegosouzapw/OmniRoute) | Local AI gateway routing 291+ providers | Machine-level app | **Documented, not committed** — optional; would redirect Claude Code away from Anthropic |
| [headroom](https://github.com/headroomlabs-ai/headroom) | Token/context compression (lib / proxy / MCP / wrapper) | Machine-level tool | **Documented, not committed** — optional cost/latency optimization |

**Why the split:** a repository can only carry skills, plugin declarations,
hooks, and settings. OmniRoute and headroom are programs that run on the operator's
machine (a local server and a local proxy/wrapper). Committing an active redirect
to `http://localhost:20128` or a local proxy into shared settings would break
Claude Code for anyone who cloned the repo without those services running — a
footgun. They are documented here with setup steps instead.

---

## What was changed in this repo

```
VPT/
├── CLAUDE.md                                  # project context + Task Observer activation
├── README.md                                  # updated: points here
├── .claude/
│   ├── settings.json                          # marketplaces + enabled plugins + permissions
│   └── skills/
│       └── task-observer/                      # vendored skill (CC BY 4.0)
│           ├── SKILL.md
│           ├── USER-GUIDE.md
│           ├── LICENSE.txt
│           ├── NOTICE.md                        # attribution + provenance
│           └── references/
│               ├── weekly-review.md
│               ├── skill-authoring.md
│               └── environments.md
└── docs/
    └── claude-code-integration-review.md       # this document
```

`.claude/settings.json` declares two plugin marketplaces and enables two plugins:

```json
{
  "extraKnownMarketplaces": {
    "claude-plugins-official": { "source": { "source": "github", "repo": "anthropics/claude-plugins-official" } },
    "claude-mem":              { "source": { "source": "github", "repo": "thedotmack/claude-mem" } }
  },
  "enabledPlugins": {
    "claude-code-setup@claude-plugins-official": true,
    "claude-mem@claude-mem": true
  }
}
```

When you open this repo in Claude Code, it will prompt you to **trust** the new
marketplaces/plugins before enabling them — that is expected and safe to accept.

---

## Per-project review

### 1. Task Observer — "One Skill to Rule Them All" — **WIRED UP**

**What it is.** A meta-skill (SKILL.md + three reference files) that watches a work
session, notices friction and repeatable procedures, and captures them as
candidate reusable skills — including improvements to itself. Licensed CC BY 4.0.

**Fit for VPT (high).** Title work is full of repeatable, checklist-driven
procedures (commitment prep, exception clearing, policy issuance). Task Observer is
exactly the tool for turning "how we did this deal" into "the skill we run every
time," which compounds in value for an ops-heavy business.

**How it was incorporated.**
- Vendored verbatim into `.claude/skills/task-observer/` so every session has it
  with no install step. Attribution and license preserved in `NOTICE.md` and
  `LICENSE.txt`.
- The skill's own docs warn that description-based auto-triggering is not
  enforceable; it recommends a `CLAUDE.md` instruction or a session-start hook. We
  added the `CLAUDE.md` instruction (see the "Task Observer activation" section
  there). A session-start hook is an equally valid alternative if you prefer
  harness-level enforcement.

**Operating notes / risks.**
- The skill keeps an observation log on a **stable** path (not an ephemeral
  checkout). In this managed remote environment the working directory is
  ephemeral, so persistence of the log across sessions depends on either committing
  it or using claude-mem — see the skill's `references/environments.md`.
- **Confidentiality:** the skill distinguishes generalizable (shareable)
  observations from project-specific ones. For a title business, strip all
  client/deal identifiers from anything recorded.

### 2. claude-mem — persistent memory — **WIRED UP**

**What it is.** A Claude Code plugin that captures session activity, compresses it
with AI, and injects relevant context into future sessions via five lifecycle
hooks (SessionStart, UserPromptSubmit, PostToolUse, Stop, SessionEnd). Storage is
local SQLite + a Chroma vector index.

**Fit for VPT (high).** Cross-session memory of deal context, prior decisions, and
recurring parties is directly useful for ongoing title files. Pairs naturally with
Task Observer (memory of *what happened* vs. skills for *how to do it*).

**How it was incorporated.**
- Declared the `claude-mem` marketplace and enabled the `claude-mem` plugin in
  `.claude/settings.json`.

**Prerequisite (machine-level, one time):**
```bash
npx claude-mem install
```
This creates `~/.claude-mem/settings.json`, the local database, and the worker.
Alternatively, install purely via the plugin marketplace:
```text
/plugin marketplace add thedotmack/claude-mem
/plugin install claude-mem
```

**Operating notes / risks.**
- Its hooks run on every session; if the worker/deps aren't installed the hooks
  can error. Run the install once per machine before relying on it.
- **Privacy is the headline concern for a title business.** claude-mem persists
  session content locally and offers `<private>` tags plus optional cloud sync.
  **Keep cloud sync off** unless you have vetted it against your handling
  obligations for client PII and nonpublic personal information. Treat the local
  memory store as sensitive data.

### 3. claude-code-setup (Anthropic official) — **WIRED UP**

**What it is.** A read-only Anthropic skill/plugin that analyzes a codebase and
recommends the top 1–2 Claude Code automations per category (MCP servers, skills,
hooks, subagents, slash commands). It recommends; it does not modify files.

**Fit for VPT (medium, one-time).** Useful as a periodic "what else should we
automate?" pass as the repo grows. Low risk because it is read-only and
first-party.

**How it was incorporated.**
- Declared the official marketplace (`anthropics/claude-plugins-official`) and
  enabled `claude-code-setup@claude-plugins-official` in `.claude/settings.json`.

**How to use.** In a session, ask: *"recommend automations for this project"* or
*"help me set up Claude Code."* Revisit after the repo accumulates real document
workflows so its recommendations have something to analyze.

### 4. OmniRoute — AI gateway router — **DOCUMENTED, NOT COMMITTED**

**What it is.** A local, open-source AI gateway (default `http://localhost:20128`)
that unifies 291+ providers behind one OpenAI-compatible endpoint, with routing
strategies, fallback, and large free tiers.

**Fit for VPT (low / optional).** It is a **cost and availability** tool, not an
ops tool. Two cautions specific to a title business:
1. Title and legal documents demand high-quality, consistent model output;
   auto-routing to arbitrary free providers trades that away.
2. Routing client documents through third-party providers has **confidentiality
   implications** that must be cleared before use.

**Why not committed.** Baking `ANTHROPIC_BASE_URL=http://localhost:20128` into
shared settings would break Claude Code for anyone without OmniRoute running.

**If you choose to use it (machine-level).**
```bash
npm install -g omniroute
omniroute                      # starts the gateway on http://localhost:20128
```
Then point Claude Code at it by setting environment variables **on your machine**
(not in the repo):
```bash
export ANTHROPIC_BASE_URL="http://localhost:20128"
export ANTHROPIC_AUTH_TOKEN="<endpoint key from the OmniRoute dashboard>"
```
Both variables are recognized by Claude Code. Start with a high-quality
provider/model rather than blind `auto` routing for document work.

### 5. headroom — context compression — **DOCUMENTED, NOT COMMITTED**

**What it is.** A token/context compressor (Rust core, Python/TS bindings) that
shrinks tool outputs, logs, and files before they reach the model — runnable as a
library, a local proxy, a CLI wrapper, or an MCP server.

**Fit for VPT (low / optional).** Potentially relevant only if you routinely feed
**very large** documents (long title chains, bulk exports) and want to cut token
cost/latency. For typical single-document review it adds moving parts without much
payoff.

**Why not committed.** Like OmniRoute, its useful modes (proxy/wrapper) run on the
operator's machine; a committed proxy redirect would break clones.

**If you choose to use it (machine-level).**
```bash
pip install "headroom-ai[all]"
headroom wrap claude           # run Claude Code through the compressor
# or run it as an MCP server:
headroom mcp serve
```
If you adopt the MCP-server mode long-term, that *can* be added to the repo later
as an MCP entry in settings — but only once the service is a standard part of every
operator's environment.

---

## Recommended rollout order

1. **Task Observer** — already in the repo; start invoking it each session (the
   `CLAUDE.md` instruction covers this). Zero external dependencies.
2. **claude-mem** — run `npx claude-mem install` once per machine, confirm cloud
   sync is **off**, then let it run. Highest ongoing payoff for VPT.
3. **claude-code-setup** — run one analysis pass now, and again after real
   workflows accumulate.
4. **OmniRoute / headroom** — evaluate only if cost, rate limits, or very large
   documents become real pain points, and only after clearing the confidentiality
   questions for client data.

## Open questions to confirm before relying on the memory/routing tools

- Are there written obligations governing where client PII / nonpublic personal
  information may be stored or transmitted? These gate cloud sync (claude-mem) and
  any third-party routing (OmniRoute, headroom).
- Should the Task Observer observation log be **committed** to the repo (durable,
  shared, but visible to anyone with repo access) or kept in claude-mem / a stable
  local path? Pick one so observations don't get lost between the ephemeral remote
  sessions.

---

*Sources reviewed: the README/skill files of each project's GitHub repository and
the Claude Code settings/plugin-marketplace documentation, on 2026-08-10.*
