# VPT Compliance Infrastructure

Version-controlled compliance system for **Vantage Point Title, Inc.** (Clearwater, FL).
This repo is the **tracking + working layer**; the document source of record remains
SharePoint/OneDrive. Built from the Compliance Dashboard Input Package (M. Buzek, 6/11/2026),
reconciled with the prior Compliance Officer's (Shelly White) shared Insurance/Bonds folders
and the NM OSI email thread.

_Last reconciled: 2026-07-23._

## What's here

| File | What it tracks |
|---|---|
| `calendar/master-calendar.csv` | **THE date tracker** — every dated obligation (bonds, filings, audits, insurance) in one chronological list. Sort by Due Date. |
| `registers/surety-bonds.csv` | 17 surety bonds / 14 states / $1,895,000. Bond #, amount, renewal date, filing method, status. |
| `registers/filings-register.csv` | 40 state filings/reports. Regulator, due date, frequency, status, owner. |
| `registers/insurance-policies.csv` | Insurance program (E&O, Cyber, Crime/Fidelity ESB, D&O, EPLI, WC, GL, Umbrella, BOP) from Shelly's folder. |
| `registers/physical-locations.csv` | 8 VPT offices by state, mapped against licensing footprint (flags AL/AR/LA gap). |
| `open-items.md` | Live issue tracker — what needs a decision, confirmation, or action, with owners. |
| `document-vault-plan.md` | Vault folder structure + inventory of Shelly White's shared folders (handoff). |
| `correspondence/NM-AECPR-penalty-mitigation-DRAFT.md` | Drafted letter held in reserve for the NM penalty. |

## How to use it

1. **Weekly:** sort `master-calendar.csv` by Due Date; work anything inside a 60-day window. Bonds and NM filings have **no grace** — treat their dates as hard.
2. **On any filing/renewal:** update the item's `Status` in the register AND the calendar. Keep both in sync.
3. **New obligation discovered:** add a row to the relevant register + the master calendar. Never let a date live only in someone's head or inbox.
4. **Open items:** review `open-items.md` at every working session; move resolved items to 🟢 (keep for the record, don't delete).

## Immediate priorities (as of 2026-07-23)

1. 🔴 **NM AECPR penalty** — mitigation letter in reserve; watch OSI inbox.
2. 🟠 **Verify OR filed** — bond (6/26), license (6/30), annual report (3/31) all passed with unconfirmed status.
3. 🟠 **Bonds due now** — IA (7/25), ID (7/27), TX Escrow Officers (7/27); confirm HUB continuations issued.
4. 🟠 **CA UTC Q2 (7/30)** and the open CA DOI audit inquiry (OASIS access gap).
5. 🔴 **AL/AR/LA offices** — physical presence with no filings tracked; verify licensing obligations.

## Ownership

- **Compliance tracking / this repo:** [to be assigned — see role question]
- **Finance / filings:** Finance Lead
- **HR / training certs / corporate:** Dan Helfrich
- **Bonds:** HUB International (Denise Edwards)
- **CPA / audits:** Ed Hill & Associates; Baker Tilly (NM AECPR); Preston CPA (WA)
- **Outsourced filings:** Compliance Freedom (Kenneth Nickel)

## Data provenance

- Filings, bonds, calendar, vault plan: Compliance Dashboard Input Package (SharePoint).
- Insurance program, office addresses, bond certificates: Shelly White shared OneDrive folders.
- NM resolution: OSI email thread (Laura Baca), 6/9-6/11/2026.
- Nothing in these files was invented; unconfirmed values are flagged `VERIFY` / `CONFIRM`.
