# VPT File & Folder Rules

The rules that keep the environment neat, tidy, and audit-ready. These are the
"particular set of rules" every user follows when creating files or folders, so
pertinent information is always logged where it belongs and stays easy to find.

## The core rules

1. **Function over person.** Files live under a site by *what they are*, not
   *whose they are*. There are **no personal folders in SharePoint** — personal
   and draft work lives in each user's **OneDrive**, which everyone already has.

2. **Name everything to the standard.** All active files follow
   `Entity_DocType_Period_[Descriptor]_[vN]` — see
   [NAMING_CONVENTION.md](NAMING_CONVENTION.md).

3. **Put it in the right site and sub-heading.** Every site has a defined set of
   sub-headings (see each site's README). Content goes under the correct
   sub-heading — not loose at the site root.

4. **Don't create new top-level folders.** The site + sub-heading structure is
   fixed and governed. If you think a new sub-heading is needed, raise it with
   the **site manager** — don't create it yourself. This is the single most
   important rule for preventing the sprawl we're fixing.

5. **Active vs. archived stay separated.** Superseded, closed, or historical
   material moves to **Legacy / Archive** — it does not sit alongside active
   files. Nothing is ever deleted (see rule 7).

6. **Version, don't duplicate.** Use the `_vN` suffix for revisions instead of
   `final`, `final2`, `FINAL-really`. The highest `vN` is current.

7. **Archived, not deleted.** No one deletes content from the old environment.
   Everything retained but inactive goes to **Legacy / Archive**. Deletion of
   any record requires explicit sign-off under a retention policy (PENDING —
   see below).

## Folder depth

Keep it shallow. **Site → Sub-heading → (optional) one grouping level → files.**
Deep nesting hides documents and defeats the point. If you're four levels deep,
the structure is wrong — raise it with the site manager.

## What good looks like

```
Finance/
  Bank & Reconciliations/
    VPT_Recon_2024-01_WellsFargo_v1.pdf
    VPT_Recon_2024-02_WellsFargo_v1.pdf
    VPT_Statement_2024-01_WellsFargo.pdf
  Revenue & Reporting/
    VPT_Report_2024_Revenue_v2.xlsx
  Audits & CPA/
    VPT_Audit_2024-Q1_CPA.xlsx
```

## What to avoid (the old pattern)

- `Dan's stuff/`, `Bots/`, `Misc/`, `New folder/`, person-name folders
- `Final_v2_USE THIS ONE.xlsx`
- The same document copied into three different sites
- Sensitive files sitting in an individual's OneDrive with no governance

## Open / PENDING items

These require input before the rules are fully final:

- **Retention policy** — how long each record type is kept before archival, and
  the (rare) conditions under which anything may ever be deleted. Requires
  leadership sign-off. Until set, the default is **archive, never delete**.
- **Sub-heading trees for several sites** — pending manager input (Dan, Brandy,
  Carolyn, Natalie, Alex). Marked PENDING in the relevant site READMEs.
