#!/usr/bin/env python3
"""VPT filename validator.

Checks filenames against the VPT naming convention:

    Entity_DocType_Period_[Descriptor]_[vN]

Segments are separated by underscores. The first three (Entity, DocType, Period)
are required; Descriptor and Version are optional. Version, if present, must be
the last segment and of the form vN.

Usage:
    python3 tools/validate_naming.py "VPT_Recon_2024-03_WellsFargo_v2.pdf"
    python3 tools/validate_naming.py --dir "/path/to/folder"
    python3 tools/validate_naming.py --dir "/path/to/folder" --recursive

Exit code is 0 if all checked names are valid, 1 otherwise — so this can be
wired into a pre-migration check or a CI step.

See governance/NAMING_CONVENTION.md for the full standard.
"""

import argparse
import os
import re
import sys

# Controlled DocType vocabulary (keep in sync with NAMING_CONVENTION.md).
DOC_TYPES = {
    "Recon", "Statement", "TaxReturn", "Audit", "Invoice", "Receipt",
    "Report", "Policy", "Contract", "Title", "Closing", "Compliance",
    "Memo", "Form",
}

# A segment: letters, digits, hyphens. No spaces, no underscores inside.
SEGMENT_RE = re.compile(r"^[A-Za-z0-9-]+$")

# Period formats: YYYY | YYYY-Qn | YYYY-MM | YYYY-MM-DD
PERIOD_RE = re.compile(r"^\d{4}(-Q[1-4]|-\d{2}(-\d{2})?)?$")

# Version: vN (v1, v2, ... v10 ...)
VERSION_RE = re.compile(r"^v\d+$")


def split_name(filename):
    """Return (stem, extension) — extension includes the leading dot, or ''."""
    root, ext = os.path.splitext(filename)
    return root, ext


def validate(filename):
    """Validate one filename. Returns (is_valid, [messages])."""
    errors = []
    warnings = []

    stem, ext = split_name(filename)

    if not stem:
        return False, ["empty filename"]

    if " " in stem:
        errors.append("contains spaces — use CamelCase or hyphens within a segment")

    segments = stem.split("_")

    if len(segments) < 3:
        errors.append(
            "fewer than 3 segments — needs at least Entity_DocType_Period"
        )
        # Still run per-segment checks on what we have.

    entity = segments[0] if len(segments) > 0 else ""
    doctype = segments[1] if len(segments) > 1 else ""
    period = segments[2] if len(segments) > 2 else ""
    extras = segments[3:] if len(segments) > 3 else []

    # Entity
    if entity and not SEGMENT_RE.match(entity):
        errors.append(f"Entity '{entity}' has invalid characters")

    # DocType
    if doctype:
        if not SEGMENT_RE.match(doctype):
            errors.append(f"DocType '{doctype}' has invalid characters")
        elif doctype not in DOC_TYPES:
            warnings.append(
                f"DocType '{doctype}' is not in the controlled list "
                f"(add it to NAMING_CONVENTION.md first if it's legitimate)"
            )

    # Period
    if period and not PERIOD_RE.match(period):
        errors.append(
            f"Period '{period}' is not YYYY, YYYY-Qn, YYYY-MM, or YYYY-MM-DD"
        )

    # Extras: optional Descriptor and/or trailing version.
    for i, seg in enumerate(extras):
        if not SEGMENT_RE.match(seg):
            errors.append(f"Segment '{seg}' has invalid characters")
            continue
        looks_like_version = seg[0] in "vV" and seg[1:].isdigit()
        is_last = i == len(extras) - 1
        if looks_like_version:
            if not VERSION_RE.match(seg):
                errors.append(
                    f"Version '{seg}' must be lowercase vN (e.g. v1, v2)"
                )
            elif not is_last:
                errors.append(f"Version '{seg}' must be the last segment")

    if not ext:
        warnings.append("no file extension")

    messages = [f"ERROR: {m}" for m in errors] + [f"WARN:  {m}" for m in warnings]
    return len(errors) == 0, messages


def iter_files(directory, recursive):
    if recursive:
        for root, _dirs, files in os.walk(directory):
            for f in files:
                yield os.path.join(root, f)
    else:
        for f in sorted(os.listdir(directory)):
            full = os.path.join(directory, f)
            if os.path.isfile(full):
                yield full


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Validate filenames against the VPT naming convention."
    )
    parser.add_argument("names", nargs="*", help="filename(s) to validate")
    parser.add_argument("--dir", help="validate every file in this directory")
    parser.add_argument(
        "--recursive", action="store_true", help="recurse into subdirectories (with --dir)"
    )
    args = parser.parse_args(argv)

    targets = list(args.names)
    if args.dir:
        targets.extend(iter_files(args.dir, args.recursive))

    if not targets:
        parser.print_help()
        return 1

    all_valid = True
    for path in targets:
        name = os.path.basename(path)
        valid, messages = validate(name)
        status = "OK  " if valid and not messages else ("OK* " if valid else "FAIL")
        print(f"[{status}] {name}")
        for m in messages:
            print(f"        {m}")
        if not valid:
            all_valid = False

    print()
    print("Legend: OK = valid, OK* = valid with warnings, FAIL = invalid")
    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())
