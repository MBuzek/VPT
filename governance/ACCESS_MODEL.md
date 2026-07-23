# VPT Access Model — DRAFT

> **STATUS: DRAFT — NOT YET APPROVED.** This model must be signed off by
> leadership **before any migration begins**. Permissions are the highest-risk
> area of this project. PremierOne (P1) configures permissions; they do not set
> policy — this document is the policy P1 implements.

## Access tiers

| Tier | Who | What they get |
|------|-----|---------------|
| **Owners** | Natalie, Alex | Full control, all sites |
| **Site Managers** | Michael Buzek, Dan, Brandy, Carolyn | Manage/edit their assigned sites |
| **Departmental staff** | Staff assigned to a function | **Contribute** (upload / create folders) **in their own department site only** |
| **General staff** | All employees, baseline | **View-only** on shared, non-restricted content — can look, cannot create folders or edit |
| **Personal** | All employees | OneDrive only — **no personal folders in SharePoint** |

**In plain terms:** rank-and-file can *see* but not *touch*; only upper-tier and
the relevant department can *contribute*; personal work stays in OneDrive.

## Restricted sites

Two sites are **restricted** and are **not** part of the "general staff can
review" bucket. General staff should not see them at all:

- **Management** — Owners + Site Managers only
- **HR** — Owners + HR department only

## Legacy / Archive access

**Recommendation (PENDING confirmation):** view-only for Owners, Site Managers,
and department heads — **not** general staff — until the archive is triaged and
cleaned, since it holds both old reference material and sensitive legacy files.
Open it up more broadly later if a need arises.

## Cross-department access

**Recommendation (PENDING confirmation):** a departmental staffer contributes in
their *own* site and is **view-only** on other non-restricted sites; **no
access** to restricted sites. Keeps collaboration easy without exposing
sensitive content.

## Open items requiring sign-off

- [ ] Confirm Management & HR excluded from all-staff view *(recommended: yes)*
- [ ] Confirm Legacy/Archive limited to upper tier + dept heads *(recommended: yes)*
- [ ] Confirm cross-department = view-only on non-restricted *(recommended: yes)*
- [ ] **Carolyn = full Site Manager rights** — logged here for sign-off
- [ ] Departed-user accounts (from the 50-account admin review) reassigned or
      removed before migration
- [ ] Final leadership sign-off on this model **before migration**

## Shared Password Archive (IT site)

A separate governed access group, tracked with the IT site. See
[`sites/7_IT/README.md`](../sites/7_IT/README.md).

- **Access group (6):** Natalie, Alex, Michael, Dan, Brandy, Carolyn
- **Scope:** shared vendor/utility logins only (e.g., FedEx) — **no** privileged/
  admin or client-fund credentials
- **MFA:** enforced tenant-wide (Microsoft Authenticator) — confirmed
- **Tool direction:** SharePoint list under IT → Password Manager (governance) —
  free/native. **Contingent on P1 pricing** for a managed alternative.
- Final implementation decision deferred to Dan, Natalie, Alex, and P1.
