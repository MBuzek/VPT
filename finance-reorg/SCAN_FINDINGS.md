# Finance Scan — Findings

*Live scan of the SharePoint environment, focused on Bank Reconciliations, Bank
Statements, and Audits. This is the evidence base for the reorg spec and
migration map in this folder.*

## Where Finance content actually lives

Content is spread across **at least three sites, three separate document
libraries, and personal OneDrives**:

| Location | Role |
|----------|------|
| `Accounting_TeamSite` → *Shared Documents* → `Accounting/` | The main pile (active + legacy intermixed) |
| `Accounting_TeamSite` → *Bank United 2026 Bank Statements* (own library) | Stray statements library |
| `Accounting_TeamSite` → *2025 BANK STATEMENTS* (own library) | Stray statements library |
| `AllStaff_TeamSite` → `VPT_Shared/` | Old audits, duplicated |
| `VPTSharepointNew2026` | Dan's new refresh site |
| Personal OneDrives (e.g. mbuzek) | Live audit working files |

Search-level scale in these three areas alone: **~358** folders matching
"reconciliation", **~1,674** matching "bank", **~9,546** matching "audit".

## Top level of `Accounting/` (the active library)

The root mixes **active recs, active audits, legacy entities, person-name dumps,
vendor/ops, and loose sensitive files** with no separation. Notable folders:

- **Active recs/bank:** `Bank United` (15.4 GB), `Bank Recs and Stmts - Operating`,
  `Wire In Rec` (4.6 GB), `Wire in Rec Bank United`, `Monthly Wire Clearing
  Reconciliation -Brandy`
- **Audits:** `Audits` (26 GB — contains `Completed Audits` at 18 GB), plus active
  audits at root: `FATCO On-Site Audit - 2026-08-20`, `FNF Audit 113431 -
  May-July 2026`
- **Revenue/reporting:** `Order Revenue - VPT` (2.8 GB), `Remittance` (4.4 GB),
  `VPT Revenue Reports`, `General Ledgers`, `Cash Flows and Notary`
- **Person-name dumps:** `Rob` (**40.6 GB**), `Roberta` (8.7 GB), `Joni` (2.5 GB),
  `Irma` (4.1 GB), `Jean`, `Adriana`, `Kristen`, `Robert Jackson`
- **Legacy entities:** `Reliant Title-NERIO` (and, inside `Rob/`: On Demand
  Escrow, MHTR, VizionX)
- **Vendor/ops:** `Fedex`, `Invoices 2023/2024/2025`, `Bill.com issues`, `Data
  Trace Invoices`, `W9's`, `Positive pay …`, `Escheat`, `Unison`, `SnapDocs`
- **System junk:** `.lnk` shortcuts (K-drive, ResWare, "This PC"), `dbisam.lck`,
  0-byte `signature`, empty `Monthly RENT`, a `test` folder

## The active spine (good news)

Current reconciliations already sit under **`Bank United/Reconciliations/`**,
organized by entity. Active entities observed:

> **VPT · VPT of CA · VPT NG · VPG · VPTCoC · Citrus · MNT**

Current primary bank is **Bank United**; older content references **Wells Fargo**
and **Chase**. Accounts are tracked by last-four (e.g. x928 escrow, x6722
operating, x1975, x6730, x2076, x6900 …).

This spine — `Bank / Reconciliations / {Entity} / {Account} / {Year}` — is the
foundation the target structure builds on.

## The core structural problems

1. **Reconciliations are duplicated into audit folders.** `Audits` (26 GB) and
   `Completed Audits` (18 GB) largely overlap with `Bank United/Reconciliations`
   (15 GB) — the same recs copied into every audit that references them. This is
   why "audit" returns ~9,546 folders. **Root cause.**
2. **Bank statements fragmented four ways** — two dedicated libraries, buried
   under `Bank United/…`, inside audit folders, and in OneDrive.
3. **Person-name dumps** — entire desktops/K-drives dropped in (`Rob` at 40.6 GB;
   `Joni/Desktop/Desktop/k drive/…`).
4. **Active and legacy intermixed** — current Bank United recs sit beside
   Reliant/NERIO, On Demand, MHTR, VizionX, Robert Jackson-era material.
5. **Inconsistent naming + typos** — `VPT Fidelety Audit 2015-3`, `VPE Washngton
   Audit 2018`, account-only folders like `x1975`.

## ⚠️ Flags requiring attention before any move

- **Live on-site audit in progress:** `FATCO On-Site Audit - 2026-08-20`, plus
  active `FNF Audit 113431 - May-July 2026`. **Freeze audit-source folders until
  FATCO clears.**
- **Sensitive files loose in the accounting root:** salary and PII spreadsheets —
  `Josh's-Rob's VP Salaries … Natalie's.xlsx`, `AdHocReport … Carolyn Guenther
  life change event.xlsx`, `Copy of Employees Josh list vs Paychex …`. These do
  not belong in a department-wide Finance site — route to restricted HR/Management.
- **Financial statements filed under HR:** `VPTSharepointNew2026 → HR/Employee
  Files/Morgan, Alexander/Bank Statements` — review who filed and where it belongs.
- **Audit source in personal OneDrive** — `FATCO AUDIT JULY 2026`, `CA AUDIT - DE
  LA VEGA`, `AZ 12.31.25 …/1. Bank Recs` in mbuzek OneDrive; should live in the
  Finance site.
