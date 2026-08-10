# Using Task Observer outside Claude Code (Cowork + the Claude app)

Task Observer is a *skill*, so it travels beyond Claude Code. The same skill
folder that lives in `.claude/skills/task-observer/` can be uploaded to Cowork and
to the regular Claude app. A ready-to-upload `task-observer.zip` is produced from
that folder (ask Claude Code to regenerate it any time, or zip the folder
yourself).

The **methodology** works identically everywhere. Only one thing changes between
environments: **where its notes get saved.**

| Environment | Notes persist automatically? | How it remembers |
|---|---|---|
| Claude Code | Yes | Saves an observation log to a stable project path |
| Cowork | Yes | Saves the log to the shared workspace folder |
| Claude app (web/desktop/phone) | No | "Handoff-doc mode" — hands you a summary to paste into the next chat |

---

## Option A — Cowork (recommended if you're not using Claude Code)

Cowork can save files, so Task Observer keeps a real memory here — nearly the same
experience as Claude Code.

1. Add the skill to Cowork by pointing it at the `task-observer/` folder (or
   uploading `task-observer.zip` if your Cowork setup takes a zip).
2. Add this one-line instruction to your Cowork project/workspace instructions so
   it activates reliably (skills don't always self-trigger while Claude is busy):

   > At the start of any task-oriented session, invoke the task-observer skill
   > before beginning work, and check the observation log for open observations.

3. Work normally. It saves its notes to the shared folder and reuses them next
   time.

## Option B — the Claude app (claude.ai / desktop / phone)

The app doesn't keep files between chats, so Task Observer runs in **handoff-doc
mode**: it collects notes during the chat and, when you're wrapping up, hands you
a summary block to save. You paste that block at the start of your next chat so it
picks up where it left off.

1. Upload the skill: **Settings → Capabilities → Skills → upload
   `task-observer.zip`** (label may vary slightly by plan/version). If you don't
   see a Skills option, your account may not have custom skills enabled yet.
2. Put the same one-line activation instruction in your **Project instructions**
   (create a Project for your title work and keep it there):

   > At the start of any task-oriented session, invoke the task-observer skill
   > before beginning work. When the session winds down, give me a handoff
   > document I can paste into the next chat.

3. At the end of a session, save the handoff block it gives you. Paste it in at the
   start of the next one.

---

## The one instruction that makes it reliable (all environments)

Skills can be missed when Claude is deep in a task, so pair the skill with a
written instruction in whatever "always-on instructions" your environment has
(CLAUDE.md in Claude Code, project/workspace instructions elsewhere):

```
At the start of any task-oriented session — any interaction where you will use
tools and produce deliverables — invoke the task-observer skill before beginning
work. When loading any skill, check the observation log for OPEN observations
tagged to that skill and apply their insights to the current work.
```

## A note for title work

Task Observer separates *shareable* method notes from *client-specific* details.
Keep everything it records generalizable — strip names, addresses, file numbers,
and any other deal-identifying information before it goes into a log or a handoff
document, especially in the app where you'll be pasting summaries around.
