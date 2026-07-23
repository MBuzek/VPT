# VPT Document Vault Plan + Source Inventory

_As of 2026-07-23. Consolidates the Dashboard Vault Plan with an inventory of Shelly White's
shared OneDrive folders so nothing from the prior Compliance Officer is lost in the handoff._

## A. Folder structure (target)

Create a top-level **States** folder in the Document Vault, one subfolder per state (all 50 + DC).
Within each active state, use a consistent template:

```
States/<State>/
  ├── Licenses
  ├── Bonds
  ├── Filings & Reports
  ├── Financials
  └── Correspondence
```

States with no current VPT activity stay as empty placeholders until needed.

**Active states** (flag by current VPT activity): AZ, CA, DC, FL, ID, IA, KS, MD, NE, NM, OH, OR, PA, TN, TX, UT, VA, WA — **plus review AL, AR, LA and NV** (physical offices and/or entities; see open item #8).

## B. Company-wide folders (in addition to States)

```
Insurance/            (E&O, Cyber, Crime/Fidelity ESB, D&O, EPLI, WC, GL, Umbrella, BOP)
Bonds/                (surety bond certificates + schedules)
Corporate/            (formation, foreign qualifications, registered agents)
Correspondence/       (regulator letters, notices, e.g. NM OSI)
```

## C. Shelly White handoff inventory (shared OneDrive)

The prior Compliance Officer (Shelly White, swhite@vptitle.net) shared her folders.
These are the compliance-relevant sources now folded into this role. **Source of record remains
SharePoint/OneDrive; this repo is the tracking + working layer.**

### `Shelly/Insurance/` — the insurance program (NET-NEW to dashboard)
- **Root policies:** Cyber (all locations), EPLI (76KDFLL3RCS), D&O (VPG 6805-4241), Workers Comp (FL + CA), Business Owner (FL), Commercial Umbrella (FL), GL (TX/AL/AR/LA/UT/NV), CA Business Insurance, `Insurance Coverage Notes.docx`, `Office Addresses.xlsx`.
- **`/VPT/`** — E&O, ESB/Fidelity, CA Escrow Bond, `VPT List.xlsx`, `Invoices and Payments.xlsx`; subfolders `2025`, `Expired`, `Other`, `To Be Completed`.
- **`/VPT/To Be Completed/`** — 2024-2025 E&O + D&O applications flagged incomplete (verify, see open item #12).
- **`/VPT/Expired/`** — superseded policies (retain for history).
- **`/Bonds/`** — original bond certificates by state (AZ, DC, IA, ID, KS, NE, NM, NV, OH, OR, PA, TN x3, TX x4, VA x2), `Bond Schedule.xlsx` (older 2023-24 schedule), `VPT Surety Bond.xlsx`, `Texas Original Bonds Filed with TDI/`.
- **`/VPG/`, `/VPT of CA/`, `/Stewart/`, `/Quotes 2025/`, `/2026-2027/`, `/Invoices/`, `/Medical/`** — related entity / underwriter / quote / renewal files.

### `Shelly/Office/VPT Offices/` and `Shelly/Remittance/`
- Office documentation and remittance records — reference; review for any dated obligations.

## D. Document filing map (dashboard attachments)

| Document | Target folder |
|---|---|
| Annual Report.pdf (AZ Corp Annual Report 2026) | States/Arizona/Filings & Reports |
| Arizona Corporation Annual Report Complete.png | States/Arizona/Filings & Reports |
| Arizona Corporation Agent Consent.png | States/Arizona/Licenses |
| Vantage Point Title Inc 12.31.25 OR Compilation.pdf | States/Oregon/Financials |
| (NM) Vantage Point Title, Inc. 12-31-25.pdf (AECPR) | States/New Mexico/Filings & Reports |

## E. Reconciliation notes (source conflicts found)

1. **Bond count:** Surety register = **17 bonds across 14 distinct states** (OR, IA, ID, TX, FL, OH, TN, NE, DC, VA, NM, KS, MD, PA). Dashboard header said "13 states" — correct to 14. Total $1,895,000 reconciles. ✓
2. **Bond schedules:** Shelly's `Bond Schedule.xlsx` is an older (2023-24) tracking sheet listing only 13 bonds. The HUB schedule (Denise Edwards, 6/5/2026) in the dashboard is the current source of record (17 bonds, 2025-2026 dates). Use HUB as authoritative.
3. **'VPT List.xlsx'** is an insurance/bond schedule, NOT a filing-status list — do not use it to drive filing "complete" flags.
