#!/usr/bin/env python3
"""Validate handbook/catalog.yaml and entity frontmatter."""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook"
CATALOG = HANDBOOK / "catalog.yaml"
REPOS = HANDBOOK / "repositories"

EVIDENCE_RE = re.compile(
    r"^(?P<repo>[A-Za-z0-9_.\-]+)@(?P<sha>[0-9a-f]{40}):(?P<path>.+)$"
)
HEX40 = re.compile(r"^[0-9a-f]{40}$")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

REQUIRED = {"id", "type", "repository", "status", "evidence"}
VALID_TYPES = {"flow", "interface", "capability", "service", "module"}
VALID_STATUS = {"established", "uncertain", "deprecated"}
VALID_CATALOG_STATUS = {"pending", "ready", "blocked"}


def load_catalog() -> dict:
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "repos" not in data:
        raise SystemExit("catalog.yaml must have top-level repos:")
    return data["repos"]


def parse_frontmatter(text: str) -> dict | None:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    data = yaml.safe_load(m.group(1))
    return data if isinstance(data, dict) else None


def check_evidence(items: list, *, entity_path: Path) -> list[str]:
    errors: list[str] = []
    if not items:
        errors.append(f"{entity_path}: evidence must be non-empty")
        return errors
    for raw in items:
        if not isinstance(raw, str):
            errors.append(f"{entity_path}: evidence item must be string")
            continue
        m = EVIDENCE_RE.match(raw.strip())
        if not m:
            errors.append(
                f"{entity_path}: bad evidence '{raw}' "
                "(want repo@40hex:path[#symbol])"
            )
            continue
        if not HEX40.match(m.group("sha")):
            errors.append(f"{entity_path}: sha must be 40 hex chars")
    return errors


def main() -> int:
    errors: list[str] = []
    repos = load_catalog()

    for repo_id, meta in repos.items():
        if not isinstance(meta, dict):
            errors.append(f"catalog {repo_id}: must be a mapping")
            continue
        for key in ("github", "wave", "status"):
            if key not in meta:
                errors.append(f"catalog {repo_id}: missing {key}")
        status = meta.get("status")
        if status not in VALID_CATALOG_STATUS:
            errors.append(f"catalog {repo_id}: invalid status {status!r}")

        folder = REPOS / repo_id
        if status == "ready":
            if not folder.is_dir():
                errors.append(f"{repo_id}: status ready but folder missing")
                continue
            md_files = [
                p
                for p in folder.rglob("*.md")
                if p.name != "README.md"
            ]
            if not md_files:
                errors.append(f"{repo_id}: status ready but no entity .md files")
            for path in md_files:
                fm = parse_frontmatter(path.read_text(encoding="utf-8"))
                if fm is None:
                    errors.append(f"{path}: missing YAML frontmatter")
                    continue
                missing = REQUIRED - set(fm)
                if missing:
                    errors.append(f"{path}: missing keys {sorted(missing)}")
                if fm.get("type") not in VALID_TYPES:
                    errors.append(f"{path}: invalid type {fm.get('type')!r}")
                if fm.get("status") not in VALID_STATUS:
                    errors.append(f"{path}: invalid status {fm.get('status')!r}")
                if fm.get("repository") != repo_id:
                    errors.append(
                        f"{path}: repository {fm.get('repository')!r} "
                        f"!= catalog key {repo_id!r}"
                    )
                evid = fm.get("evidence")
                if not isinstance(evid, list):
                    errors.append(f"{path}: evidence must be a list")
                else:
                    errors.extend(check_evidence(evid, entity_path=path))

        elif status == "pending" and folder.is_dir():
            # Optional early entities OK while pending
            pass

    # _example must never be in catalog as ready
    if "_example" in repos and repos["_example"].get("status") == "ready":
        errors.append("_example must not be status ready")

    if errors:
        print("FAIL:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"OK: catalog {len(repos)} repos; handbook schema checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
