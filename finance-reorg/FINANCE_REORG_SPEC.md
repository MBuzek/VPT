# Finance Site — Reorg Spec

*Target structure for a clean, modern Finance site: easier to pull reports,
easier to save them, and audit-ready. Grounded in the live scan
([SCAN_FINDINGS.md](SCAN_FINDINGS.md)); migration detail in
[MIGRATION_MAP.csv](MIGRATION_MAP.csv).*

## The one principle that fixes the mess

**Reconciliations and Bank Statements are the source of truth and live once.
Audits reference them — they never become their home.**

Today recs are copied into every audit folder, which is why `Audits` (26 GB),
`Completed Audits` (18 GB), and `Bank United/Reconciliations` (15 GB) overlap so
heavily. New rule: a rec exists in exactly one place; an audit links to it (or
takes a dated snapshot only when an auditor requires a frozen copy). This single
change collapses the ~9,546-folder audit sprawl.

## Target structure

```
Finance
│
├── 01 Bank Reconciliations          ← source of truth (from Bank United/Reconciliations)
│    └── {Entity}                      VPT · VPT of CA · VPT NG · VPG · VPTCoC · Citrus · MNT
│         └── {Account xNNNN}          e.g. Escrow x928, Operating x6722
│              └── {Year}
│                   VPT_Recon_2024-03_Escrow-x928_v1.pdf
│
├── 02 Bank Statements               ← consolidate the two stray libraries + audit copies
│    └── {Entity} → {Account xNNNN} → {Year}
│         VPT_Statement_2024-03_Escrow-x928.pdf
│
├── 03 Wire Reconciliations          ← Wire In Rec, Wire in Rec Bank United, Monthly Wire Clearing
│    └── {Year}
│
├── 04 Audits & Exams                ← events; reference the libraries above
│    ├── Active
│    │    └── {Auditor–Scope–Period}   e.g. "FATCO On-Site 2026-08"
│    │         ├── 00 Request & Correspondence
│    │         ├── 01 Three-Way Reconciliations
│    │         ├── 02 Bank Statements
│    │         └── 03 Working Papers & Findings
│    └── Completed → {Year} → {Auditor–Scope}
│
├── 05 Revenue & Reporting           ← consolidate scattered reports
│    ├── Order & Remittance Revenue    (Order Revenue - VPT, Remittance, VPT Revenue Reports)
│    ├── Cash Flow
│    └── General Ledgers
│
└── 06 Accounting Operations         ← AP/vendor/bank-admin that isn't recs/statements/audits
     ├── Invoices & AP                 (Invoices 2023–2025, Bill.com, Data Trace, vendor stmts)
     ├── Bank Admin                    (signers, signature cards, account lists, positive pay)
     ├── Escheat & Unclaimed
     └── Wire Instructions
```

Anything **legacy** (Reliant/NERIO, On Demand, MHTR, VizionX, Robert Jackson era,
old completed audits, person-name dumps after extraction) goes to
**Legacy / Archive** — *archived, not deleted*. Anything **sensitive/misfiled**
(loose salary/PII) routes to **restricted HR/Management**, never the department
Finance site.

## The "easier to pull reports" layer — metadata + views

Folders alone can't answer "give me every three-way rec for Q2 2026." So on the
**Bank Reconciliations** and **Bank Statements** libraries, add columns and let
saved Views do the work:

| Column | Values |
|--------|--------|
| Entity | VPT, VPT of CA, VPT NG, VPG, VPTCoC, Citrus, MNT |
| Account | last-four (x928, x6722, …) |
| Bank | Bank United, Wells Fargo, Chase |
| DocType | Reconciliation, Statement, Three-Way, Support |
| Period | date (month-end) |
| Status | Active, Archived |

**Saved views** then become one-click report pulls, e.g.:
- *"All three-way recs — Q2 2026 — all accounts"* (audit package)
- *"Everything for account x928 — 2024"*
- *"VPT of CA — statements — this year"*

This is the modern win: save by dragging into the right library and tagging;
retrieve by filtering, not folder-digging.

## Naming standard (applied)

`Entity_DocType_Period_[Descriptor]_[vN]` — machine-sortable, audit-legible:

| Example | Reads as |
|---------|----------|
| `VPT_Recon_2024-03_Escrow-x928_v2.pdf` | VPT reconciliation, Mar 2024, escrow x928, v2 |
| `VPT_Statement_2024-03_Operating-x6722.pdf` | VPT statement, Mar 2024, operating x6722 |
| `VPTofCA_ThreeWay_2026-Q2_FATCO.xlsx` | VPT of CA three-way rec, Q2 2026, for FATCO |

Legacy content is exempt — preserved as-is, renamed only if promoted back to
active use.

## Sequencing (nothing moves until sign-off + FATCO clears)

1. **Confirm the four decisions** (below) and get the target site from Dan.
2. **Freeze** audit-source folders through the FATCO on-site audit (2026-08-20).
3. **Provision** the empty target structure + columns/views (safe — touches no
   live files).
4. **Move active recs/statements** into the new libraries, applying naming.
5. **Reparent audits** to reference the libraries; move Completed Audits to
   Legacy by year.
6. **Triage person-name dumps** — extract anything active, archive the rest.
7. **Route sensitive/misfiled** files to restricted sites.

## Open decisions (need Michael/Dan)

1. **Target site** — build in `VPTSharepointNew2026` (Dan's refresh) or the
   existing `Accounting_TeamSite`? *(Coordinate with Dan — he owns the refresh.)*
2. **Primary axis** — Entity → Account → Year *(recommended)*, or Account first?
3. **Active vs legacy entity list** — confirm VPT / VPT of CA / VPT NG / VPG /
   VPTCoC / Citrus / MNT are active; Reliant, On Demand, MHTR, VizionX → Legacy.
4. **Metadata + views** — adopt the metadata layer *(recommended)* or start
   folders-only?
