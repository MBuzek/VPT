# Legacy / Archive

**Purpose:** The permanent home for everything retained from the old environment
that isn't part of the clean, active structure — old files, prior-regime
materials, and anything not special or actively needed but worth keeping.

> **This is the "Legacy folder" done right.** It's the single destination for
> old-SharePoint content so active sites stay clean and audit-ready, while
> nothing of record is ever lost.

**Access:** Owners, Site Managers, and department heads — view-only
(PENDING confirmation). Not general staff, until triaged.

## The governing principle: **Archived, not deleted**

Nothing from the old environment gets destroyed. If content is inactive,
superseded, or of uncertain value, it comes **here** rather than being deleted.
Deletion of any record requires explicit sign-off under a retention policy
(PENDING) — the default is *keep*.

## Recommended structure

Organize by **origin** so provenance is preserved and things stay findable:

- **Robert Jackson Era** — materials from the prior regime, kept intact
- **Old SharePoint (unsorted)** — bulk content migrated as-is from the old sites
- **By Year** — historical files grouped by year where that's the natural key
- **To Triage** — landing zone for content awaiting sorting/classification

```
Legacy_Archive/
  Robert Jackson Era/
  Old SharePoint (unsorted)/
  By Year/
    2019/
    2020/
    2021/
  To Triage/
```

## Naming

Legacy content is **exempt** from the active naming convention — we preserve
historical files as-is rather than renaming them. Once a legacy file is promoted
back into active use, rename it to the standard at that point.

## What belongs here

- Prior-regime and historical materials
- Superseded/closed records past active use but retained
- Old-SharePoint content that doesn't map cleanly to an active site (yet)

## What does NOT belong here

- Active, in-use records → their function site
- Anything requiring deletion — deletion is not this site's job; **archive,
  never delete** is the rule

## Note on the earlier failed attempt

An earlier attempt to stand up a legacy folder did not succeed. This structure
is designed to be provisioned cleanly by P1 as a proper site under the hub, with
a defined access tier and the archive-not-delete rule baked in — not a loose
folder bolted onto an existing site.
