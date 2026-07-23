# VPT SharePoint Architecture — Source of Truth

**Vantage Point Title (VPT) — Information Architecture & Governance**

This repository is the authoritative blueprint for VPT's SharePoint and OneDrive
environment. It defines *what the environment should look like*, *the rules that
keep it clean*, and *who can access what* — so the live site can be provisioned
from a single, version-controlled specification instead of being hand-assembled
and drifting over time.

> **Why this exists:** VPT's current SharePoint suffers from inconsistent
> labeling, content scattered across sites, active and legacy files intermixed,
> and no structural logic. Auditors can't pull support quickly, management can't
> find what it needs, and sensitive documents aren't adequately protected. This
> blueprint fixes the root cause: a clean, function-based structure with
> enforceable naming and access rules.

## What's here

| Path | What it defines |
|------|-----------------|
| [`sites/`](sites/) | The nine-site hub model — one folder + README per site, each describing purpose, access tier, and sub-headings |
| [`governance/NAMING_CONVENTION.md`](governance/NAMING_CONVENTION.md) | The `Entity_DocType_Period_[Descriptor]_[vN]` file-naming standard |
| [`governance/FOLDER_RULES.md`](governance/FOLDER_RULES.md) | The rules for creating files and folders so everything stays audit-ready |
| [`governance/ACCESS_MODEL.md`](governance/ACCESS_MODEL.md) | Tiered access model (DRAFT — pending leadership sign-off) |
| [`tools/validate_naming.py`](tools/validate_naming.py) | A working validator that checks filenames against the naming standard |

## The nine-site hub model

1. **Management** *(restricted)*
2. **Finance**
3. **Compliance**
4. **HR** *(restricted)*
5. **Funding**
6. **Title Operations**
7. **IT**
8. **Legacy / Archive**
9. **All Company**

## Governing principles

- **Function-based, not person-based.** Content lives under a site by *what it
  is*, not *whose it is*. No personal folders in SharePoint — personal work
  lives in OneDrive.
- **Archived, not deleted.** Nothing from the old regime gets destroyed.
  Everything retained but inactive goes to **Legacy / Archive**.
- **Named consistently.** All active content follows the naming convention so it
  is findable, sortable, and audit-ready.
- **Access before migration.** The access model must be signed off by leadership
  *before* any data is moved. Permissions are the highest-risk area of this
  project.

## Ownership & roles

- **Site owners:** Natalie, Alex
- **Site managers / heads:** Michael Buzek, Dan, Brandy, Carolyn
- **External IT partner:** PremierOne (P1) — holds SharePoint admin rights;
  required for site/hub provisioning and permission configuration.

## Status

This is a **planning and specification** repository. Provisioning the live
SharePoint site (hub creation, permissions) requires SharePoint admin rights and
is performed by PremierOne from this blueprint. Items marked **PENDING** below
require manager input or leadership sign-off before they are final.
