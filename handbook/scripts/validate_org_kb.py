#!/usr/bin/env python3
"""Validate org-handbook catalog + ready repos' entity evidence pointers.

Usage (from content-knowledge-base root):
  python org-handbook/scripts/validate_org_kb.py
Exit 0 on success; non-zero on failure.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "catalog.yaml"
REPOS_DIR = ROOT / "repositories"

_POINTER_RE = re.compile(
    # Path may contain spaces (ios "Pocket FM/...", Infra "Root Apps/...").
    r"^(?P<repo>[A-Za-z0-9_.-]+)@"
    r"(?P<sha>[0-9a-fA-F]{7,40}):"
    r"(?P<path>[^#]+)"
    r"(?:#(?P<symbol>[A-Za-z0-9_.-]+))?$"
)
# Scripts / shell entrypoints may omit #symbol; prefer symbols for source files.
_SCRIPT_SUFFIXES = (".sh", ".bash", ".yml", ".yaml", ".md", ".json", ".toml")
_FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _load_catalog() -> dict:
    if yaml is None:
        # Minimal YAML subset for our catalog (no nested lists required).
        return _load_catalog_stdlib()
    data = yaml.safe_load(CATALOG.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "repos" not in data:
        raise SystemExit("catalog.yaml: missing top-level repos")
    return data


def _load_catalog_stdlib() -> dict:
    text = CATALOG.read_text(encoding="utf-8")
    repos: dict[str, dict[str, str]] = {}
    current: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.startswith("#") or line.startswith("version:"):
            continue
        if line == "repos:":
            continue
        m = re.match(r"^  ([A-Za-z0-9_.-]+):\s*$", line)
        if m:
            current = m.group(1)
            repos[current] = {}
            continue
        if current is None:
            continue
        km = re.match(r"^    (github|wave|status|notes):\s*(.*)$", line)
        if km:
            repos[current][km.group(1)] = km.group(2).strip()
    return {"version": 1, "repos": repos}


def _parse_frontmatter(text: str) -> dict[str, object]:
    match = _FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    block = match.group(1)
    out: dict[str, object] = {}
    evidence: list[str] = []
    in_evidence = False
    for raw in block.splitlines():
        line = raw.rstrip()
        if line.startswith("evidence:"):
            in_evidence = True
            rest = line[len("evidence:") :].strip()
            if rest.startswith("[") and rest.endswith("]"):
                # inline list not used; ignore
                pass
            continue
        if in_evidence:
            if re.match(r"^\s*-\s+", line):
                evidence.append(re.sub(r"^\s*-\s+", "", line).strip().strip("\"'"))
                continue
            if re.match(r"^[a-z_]+:", line):
                in_evidence = False
            else:
                continue
        if in_evidence:
            continue
        km = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if km:
            out[km.group(1)] = km.group(2).strip().strip("\"'")
    if evidence:
        out["evidence"] = evidence
    return out


def _validate_entity(path: Path, repo_id: str, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    meta = _parse_frontmatter(text)
    for key in ("id", "type", "repository"):
        if not meta.get(key):
            errors.append(f"{path}: missing frontmatter `{key}`")
    if str(meta.get("repository") or "") != repo_id:
        errors.append(
            f"{path}: repository `{meta.get('repository')}` != catalog `{repo_id}`"
        )
    evidence = meta.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        errors.append(f"{path}: evidence list required")
        return
    for ptr in evidence:
        match = _POINTER_RE.match(str(ptr))
        if not match:
            errors.append(f"{path}: bad evidence pointer `{ptr}`")
            continue
        sha = match.group("sha")
        if len(sha) != 40:
            errors.append(f"{path}: evidence SHA must be 40 hex chars (`{ptr}`)")
        rel = match.group("path").strip()
        sym = match.group("symbol")
        if not sym and not rel.lower().endswith(_SCRIPT_SUFFIXES):
            errors.append(
                f"{path}: evidence missing #symbol for source path `{ptr}` "
                "(shell/config/docs suffixes may omit symbol)"
            )

def main() -> int:
    if not CATALOG.is_file():
        print(f"FAIL: missing {CATALOG}", file=sys.stderr)
        return 2
    try:
        data = _load_catalog()
    except SystemExit as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 2
    repos = data.get("repos") or {}
    if not isinstance(repos, dict) or not repos:
        print("FAIL: catalog repos empty", file=sys.stderr)
        return 2

    errors: list[str] = []
    ready = 0
    pending = 0
    for repo_id, meta in sorted(repos.items()):
        if not isinstance(meta, dict):
            errors.append(f"{repo_id}: entry must be a mapping")
            continue
        for req in ("github", "wave", "status"):
            if not str(meta.get(req) or "").strip():
                errors.append(f"{repo_id}: missing `{req}`")
        status = str(meta.get("status") or "").strip().lower()
        folder = REPOS_DIR / repo_id
        if status == "pending":
            pending += 1
            continue
        if status == "blocked":
            continue
        if status != "ready":
            errors.append(f"{repo_id}: unknown status `{status}`")
            continue
        ready += 1
        if not folder.is_dir():
            errors.append(f"{repo_id}: status ready but missing {folder}")
            continue
        entities = list(folder.rglob("*.md"))
        entities = [p for p in entities if p.name.upper() != "README.MD"]
        if not entities:
            errors.append(f"{repo_id}: status ready but no entity markdown")
            continue
        for path in entities:
            _validate_entity(path, repo_id, errors)

    if errors:
        print(f"FAIL: {len(errors)} error(s)", file=sys.stderr)
        for err in errors[:50]:
            print(f"  - {err}", file=sys.stderr)
        if len(errors) > 50:
            print(f"  … {len(errors) - 50} more", file=sys.stderr)
        return 1

    print(
        f"OK: {len(repos)} catalog repos "
        f"({ready} ready, {pending} pending) — validation passed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
