#!/usr/bin/env python3
"""Structural validation for org.yaml and packs/manifest.yaml."""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    errors: list[str] = []
    org = yaml.safe_load((ROOT / "org.yaml").read_text(encoding="utf-8"))
    if not isinstance(org, dict):
        raise SystemExit("org.yaml must be a mapping")

    if (org.get("organization") or {}).get("id") != "pocketfm":
        errors.append("organization.id must be pocketfm")

    repos = (org.get("sources") or {}).get("repositories") or []
    if not repos:
        errors.append("sources.repositories is empty")
    ids: set[str] = set()
    for r in repos:
        rid = r.get("id")
        if not rid:
            errors.append("repository missing id")
            continue
        if rid in ids:
            errors.append(f"duplicate repository id {rid}")
        ids.add(rid)
        if not r.get("github") and not r.get("path"):
            errors.append(f"{rid}: need github or path")

    catalog = yaml.safe_load(
        (ROOT / "handbook" / "catalog.yaml").read_text(encoding="utf-8")
    )
    catalog_ids = set((catalog or {}).get("repos") or {})
    # org may include groot extra; catalog is SoT for handbook
    missing_in_org = catalog_ids - ids
    if missing_in_org:
        errors.append(
            "org.yaml missing catalog repos: " + ", ".join(sorted(missing_in_org))
        )

    manifest = yaml.safe_load(
        (ROOT / "packs" / "manifest.yaml").read_text(encoding="utf-8")
    )
    mappings = (manifest or {}).get("mappings") or {}
    unmapped = set((manifest or {}).get("unmapped_ok") or [])
    for rid in ids:
        if rid not in mappings and rid not in unmapped:
            errors.append(f"{rid}: not in packs/manifest mappings or unmapped_ok")

    for rid, meta in mappings.items():
        contract = ROOT / meta["contract"] if "contract" in meta else None
        # contract paths in manifest are repo-relative
        if "contract" in meta:
            cpath = ROOT / meta["contract"]
            # also allow packs/<pack>/... relative as written
            if not cpath.is_file():
                alt = ROOT / meta["contract"].removeprefix("packs/")
                # manifest already includes packs/ prefix
                if not cpath.is_file():
                    errors.append(f"missing contract for {rid}: {meta['contract']}")

    policies = yaml.safe_load((ROOT / "policies.yaml").read_text(encoding="utf-8"))
    if "profiles" not in (policies or {}):
        errors.append("policies.yaml missing profiles")

    if errors:
        print("FAIL:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(
        f"OK: org.yaml {len(ids)} sources; catalog {len(catalog_ids)}; "
        f"packs manifest aligned"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
