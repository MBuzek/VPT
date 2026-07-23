# IT

**Purpose:** IT documentation, hardware inventory, PremierOne (P1) records, and
governed shared credentials.

**Access:** Departmental contribute (IT + Site Managers) + view-only for other
non-restricted tiers per the access model.

## Sub-headings (defined)

- **Hardware & Serial #s** — device inventory, serial numbers, warranties
- **P1 Documentation** — PremierOne setup docs, tickets, configurations
- **Password Manager (governance)** — the Shared Password Archive (below)

## Shared Password Archive

A centralized, governed location for **shared vendor/utility credentials** (e.g.,
FedEx and similar logins) so no individual can unilaterally change a shared
password and access stays visible to authorized staff.

**Access group (6):** Natalie, Alex, Michael, Dan, Brandy, Carolyn
— implemented as a dedicated security group (e.g., `SG-VPT-PasswordArchive`),
created by P1.

**Scope rule:** shared vendor/utility logins **only**. **No** privileged/admin
credentials and **nothing** touching client funds.

**Security baseline:** MFA enforced tenant-wide (Microsoft Authenticator).
Recognized employees in the group open the list with no extra friction; the M365
login behind it is the protection.

**Tool direction (contingent on P1 pricing):** a **SharePoint list** here under
Password Manager (governance) — free, native, with version history and audit
trail. Leadership asked for P1's price on a managed alternative first; the
SharePoint-list build proceeds only if that comes back too expensive.

**Governance:** named owner, access reviewed on the same cadence as the
50-account admin review, and shared passwords **rotated when anyone leaves the
group**. Final implementation decision deferred to Dan, Natalie, Alex, and P1.

## What belongs here

- Hardware inventory and serial numbers
- P1 documentation and IT configuration records
- Governed shared credentials (per scope rule above)

## What does NOT belong here

- Personal passwords → each user's own responsibility, never here
- Non-IT department files → their function site
