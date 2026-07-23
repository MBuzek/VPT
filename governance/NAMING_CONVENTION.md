# VPT File Naming Convention

**Standard:** `Entity_DocType_Period_[Descriptor]_[vN]`

Applied consistently to **all active content**. This is what makes files
findable, sortable, and audit-ready — an auditor or manager should be able to
locate the right document from its name alone, without opening it.

> Legacy content in the **Legacy / Archive** site is exempt (see
> [FOLDER_RULES.md](FOLDER_RULES.md)) — we do not rename historical files, we
> preserve them as-is.

## The segments

Segments are separated by underscores (`_`). The first three are **required**;
the last two are **optional**.

| Segment | Required | What it is | Format | Examples |
|---------|----------|------------|--------|----------|
| **Entity** | Yes | The company or party the document belongs to | No spaces; use CamelCase or hyphens | `VPT`, `AcmeTitle`, `SmithEstate` |
| **DocType** | Yes | The type of document | From the controlled list below | `Recon`, `TaxReturn`, `Audit` |
| **Period** | Yes | The time period the document covers | `YYYY`, `YYYY-Qn`, `YYYY-MM`, or `YYYY-MM-DD` | `2024`, `2024-Q1`, `2024-03`, `2024-03-15` |
| **Descriptor** | No | Free-text detail to disambiguate | No spaces; CamelCase or hyphens | `WellsFargo`, `FinalSigned`, `Amended` |
| **Version** | No | Version number; **must be the last segment** | `vN` (e.g. `v1`, `v2`, `v10`) | `v1`, `v3` |

### Rules

- **No spaces anywhere.** Use CamelCase (`WellsFargo`) or hyphens (`wells-fargo`)
  within a segment.
- **Underscores separate segments only** — never inside a segment.
- **Period is machine-sortable** — always lead with the four-digit year so files
  sort chronologically.
- **Version, if used, is always last** and always `vN`.
- Allowed characters within a segment: letters, digits, and hyphens.

## Controlled vocabulary — DocType

Keep this list tight. If a needed type is missing, add it here first (via the
site manager) rather than inventing a one-off — that's how sprawl starts.

| DocType | Meaning |
|---------|---------|
| `Recon` | Reconciliation |
| `Statement` | Bank / account statement |
| `TaxReturn` | Tax return |
| `Audit` | Audit file / workpaper |
| `Invoice` | Invoice |
| `Receipt` | Receipt / proof of payment |
| `Report` | Report (revenue, management, etc.) |
| `Policy` | Policy or procedure document |
| `Contract` | Contract / agreement |
| `Title` | Title document / commitment |
| `Closing` | Closing package / settlement statement |
| `Compliance` | Compliance record / filing |
| `Memo` | Internal memo |
| `Form` | Blank or completed form |

## Examples

| Filename | Reads as |
|----------|----------|
| `VPT_Recon_2024-03_WellsFargo_v2.pdf` | VPT reconciliation, March 2024, Wells Fargo account, version 2 |
| `VPT_TaxReturn_2023_Federal_FinalSigned.pdf` | VPT federal tax return, 2023, final signed |
| `VPT_Audit_2024-Q1_CPA.xlsx` | VPT audit workpaper, Q1 2024, from CPA |
| `SmithEstate_Closing_2024-05-15.pdf` | Smith Estate closing package, May 15 2024 |
| `VPT_Report_2024_Revenue_v1.xlsx` | VPT revenue report, full-year 2024, version 1 |

## Validation

Run the validator against any filename or a whole folder:

```bash
python3 tools/validate_naming.py "VPT_Recon_2024-03_WellsFargo_v2.pdf"
python3 tools/validate_naming.py --dir "/path/to/folder"
```

See [`tools/validate_naming.py`](../tools/validate_naming.py).
