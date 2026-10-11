#!/usr/bin/env python3
"""Audit org-kb entity quality beyond validate_org_kb.py.

Checks:
  - filename == {id}.md; type folder == frontmatter type
  - evidence pointers parse; prefer 40-char SHA + #symbol
  - optional: path exists in local clone map (--check-clones)

Exit 0 when no errors (warnings allowed unless --strict-warnings).
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPOS_DIR = ROOT / "repositories"
FRONT = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
PTR = re.compile(
    r"^(?P<repo>[A-Za-z0-9_.-]+)@"
    r"(?P<sha>[0-9a-fA-F]{7,40}):"
    r"(?P<path>[^#]+)"
    r"(?:#(?P<symbol>[A-Za-z0-9_.-]+))?$"
)
SCRIPT_SUFFIXES = (".sh", ".bash", ".yml", ".yaml", ".md", ".json", ".toml")

DEFAULT_CLONES = {
    "radioly_client_api": "radioly_client_api",
    "iam": "iam",
    "nexus": "nexus",
    "android_client": "android_client",
    "ios_client": "ios_client",
    "kafka-stream-clients": "kafka-stream-clients",
    "airflow": "airflow",
    "apollo": "apollo",
    "go-common": "go-common",
    "python-common": "python-common",
    "content-backend": "content-backend",
    "fabric": "fabric",
    "impression": "fabric",
    "experience": "airflow",
    "ads": "airflow",
    "go-radioly": "go-radioly-service",
    "go-radioly-service": "go-radioly-service",
    "raven": "raven",
    "writers-backend": "writers-backend",
    "cms-dashboard-backend": "cms-dashboard-backend",
    "prod_novels_cron_airflow": "prod_novels_cron_airflow",
    "writers_payout_airflow": "writers_payout_airflow",
    "litefm-backend": "litefm-backend",
    "pocket_search": "pocket_search",
    "novels-kafka-stream-client": "Novels-Kafka-Stream-Clients",
    "Novels-Kafka-Stream-Clients": "Novels-Kafka-Stream-Clients",
    "infra-deployments-k8s": "Infra_deployments_k8s",
    "Infra_deployments_k8s": "Infra_deployments_k8s",
    "infra-k8s": "Infra_k8s",
    "Infra_k8s": "Infra_k8s",
    "infra-docs": "infra_docs",
    "infra_docs": "infra_docs",
}


def parse_fm(text: str) -> dict:
    m = FRONT.match(text)
    if not m:
        return {}
    meta: dict = {}
    evidence: list[str] = []
    in_ev = False
    for raw in m.group(1).splitlines():
        line = raw.rstrip()
        if line.startswith("evidence:"):
            in_ev = True
            continue
        if in_ev:
            if re.match(r"^\s*-\s+", line):
                evidence.append(re.sub(r"^\s*-\s+", "", line).strip())
                continue
            if re.match(r"^[a-z_]+:", line):
                in_ev = False
            else:
                continue
        km = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if km:
            meta[km.group(1)] = km.group(2).strip()
    meta["evidence"] = evidence
    meta["body"] = (m.group(2) or "").strip()
    return meta


def path_ok(clone: Path, rel: str) -> bool:
    return (clone / rel).exists()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--clones-root",
        default=str(Path(__file__).resolve().parents[3]),
        help="Parent dir containing app clones (default: ../../.. from org-handbook)",
    )
    parser.add_argument("--check-clones", action="store_true")
    parser.add_argument("--strict-warnings", action="store_true")
    args = parser.parse_args()
    clones_root = Path(args.clones_root)

    errors: list[str] = []
    warnings: list[str] = []
    n_ent = n_ptr = 0

    for path in sorted(REPOS_DIR.rglob("*.md")):
        if path.name.upper() == "README.MD":
            continue
        n_ent += 1
        meta = parse_fm(path.read_text(encoding="utf-8"))
        repo_id = path.parts[path.parts.index("repositories") + 1]
        type_dir = path.parts[path.parts.index("repositories") + 2]
        eid = str(meta.get("id") or "")
        etype = str(meta.get("type") or "")
        erepo = str(meta.get("repository") or "")
        estatus = str(meta.get("status") or "")
        body = str(meta.get("body") or "")
        evidence = meta.get("evidence") or []
        rel_path = path.relative_to(ROOT)

        if eid and path.name != f"{eid}.md":
            errors.append(f"{rel_path}: filename != {eid}.md")
        if etype and type_dir != etype:
            errors.append(f"{rel_path}: folder `{type_dir}` != type `{etype}`")
        if erepo != repo_id:
            errors.append(f"{rel_path}: repository `{erepo}` != `{repo_id}`")
        if estatus not in ("established", "uncertain", "deprecated"):
            errors.append(f"{rel_path}: bad status `{estatus}`")
        if len(body) < 40:
            warnings.append(f"{rel_path}: thin body ({len(body)} chars)")
        if not evidence:
            errors.append(f"{rel_path}: no evidence")
            continue
        for ptr in evidence:
            n_ptr += 1
            m = PTR.match(str(ptr))
            if not m:
                errors.append(f"{rel_path}: bad pointer `{ptr}`")
                continue
            sha, pref, rel, sym = (
                m.group("sha"),
                m.group("repo"),
                m.group("path").strip(),
                m.group("symbol"),
            )
            if len(sha) != 40:
                errors.append(f"{rel_path}: SHA not 40 chars `{ptr}`")
            if not sym and not rel.lower().endswith(SCRIPT_SUFFIXES):
                errors.append(f"{rel_path}: missing #symbol `{ptr}`")
            if args.check_clones:
                key = pref if pref in DEFAULT_CLONES else repo_id
                sub = DEFAULT_CLONES.get(key) or DEFAULT_CLONES.get(pref)
                if not sub:
                    warnings.append(f"{rel_path}: no clone map for `{pref}`")
                    continue
                clone = clones_root / sub
                if not clone.is_dir():
                    warnings.append(f"{rel_path}: missing clone `{clone}`")
                    continue
                if not path_ok(clone, rel):
                    errors.append(f"{rel_path}: path missing in clone `{ptr}`")

    print(f"entities={n_ent} pointers={n_ptr} errors={len(errors)} warnings={len(warnings)}")
    for e in errors:
        print(f"ERROR: {e}", file=sys.stderr)
    for w in warnings[:30]:
        print(f"WARN: {w}", file=sys.stderr)
    if warnings[30:]:
        print(f"WARN: … {len(warnings)-30} more", file=sys.stderr)
    if errors:
        return 1
    if args.strict_warnings and warnings:
        return 1
    print("OK: org-kb evidence audit passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
