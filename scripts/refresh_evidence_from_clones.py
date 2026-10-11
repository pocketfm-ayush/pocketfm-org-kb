#!/usr/bin/env python3
"""Refresh handbook evidence SHAs when paths exist at local clone HEAD.

Maps catalog repository_id → sibling checkout under REPO_ROOT (default ../..
from this repo's parent Work/Repo layout).

Does not invent paths. Leaves pointers unchanged when the path is missing.
Writes a report to evaluation/baselines/evidence-refresh-report.md
"""

from __future__ import annotations

import argparse
import re
import subprocess
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HANDBOOK = ROOT / "handbook" / "repositories"
REPORT = ROOT / "evaluation" / "baselines" / "evidence-refresh-report.md"

POINTER_RE = re.compile(
    r"^(?P<repo>[A-Za-z0-9_.-]+)@"
    r"(?P<sha>[0-9a-fA-F]{7,40}):"
    r"(?P<path>[^#\n]+)"
    r"(?:#(?P<symbol>[^\n]+))?$"
)

# catalog id → local directory name under Work/Repo
CLONE_MAP = {
    "radioly_client_api": ["radioly_client_api", "radioly"],
    "iam": ["iam"],
    "nexus": ["nexus"],
    "android_client": ["android_client"],
    "ios_client": ["ios_client"],
    "kafka-stream-clients": ["kafka-stream-clients"],
    "airflow": ["airflow"],
    "apollo": ["apollo"],
    "impression": ["fabric"],
    "go-common": ["go-common"],
    "python-common": ["python-common"],
    "experience": ["airflow"],
    "content-backend": ["content-backend"],
    "ads": ["airflow"],
    "go-radioly": ["go-radioly-service"],
    "raven": ["raven"],
    "fabric": ["fabric"],
    "writers-backend": ["writers-backend"],
    "cms-dashboard-backend": ["cms-dashboard-backend"],
    "prod_novels_cron_airflow": ["prod_novels_cron_airflow"],
    "novels-kafka-stream-client": ["Novels-Kafka-Stream-Clients"],
    "writers_payout_airflow": ["writers_payout_airflow"],
    "litefm-backend": ["litefm-backend"],
    "pocket_search": ["pocket_search", "search"],
    "infra-deployments-k8s": ["Infra_deployments_k8s"],
    "infra-k8s": ["Infra_k8s"],
    "infra-docs": ["infra_docs"],
    "groot": ["groot"],
}


def git_head(clone: Path) -> str | None:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(clone), "rev-parse", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return out if len(out) == 40 else None


def path_exists_at_head(clone: Path, rel: str) -> bool:
    return (clone / rel).is_file()


def resolve_clone(repo_root: Path, catalog_id: str) -> Path | None:
    for name in CLONE_MAP.get(catalog_id, [catalog_id]):
        p = repo_root / name
        if (p / ".git").exists():
            return p
    return None


def refresh_file(path: Path, clones: dict[str, tuple[Path, str]], *, write: bool) -> Counter:
    stats: Counter = Counter()
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    changed = False
    for line in lines:
        stripped = line.strip()
        # evidence list items: "  - repo@sha:path#sym"
        m_item = re.match(r"^(\s*-\s+)(.+?)(\s*)$", line.rstrip("\n"))
        if not m_item:
            out.append(line)
            continue
        prefix, body, _ = m_item.group(1), m_item.group(2).strip(), m_item.group(3)
        pm = POINTER_RE.match(body)
        if not pm:
            out.append(line)
            continue
        repo = pm.group("repo")
        old_sha = pm.group("sha")
        rel = pm.group("path").strip()
        symbol = pm.group("symbol")
        stats["pointers"] += 1
        if repo not in clones:
            stats["no_clone"] += 1
            out.append(line)
            continue
        clone, head = clones[repo]
        if not path_exists_at_head(clone, rel):
            stats["missing_path"] += 1
            out.append(line)
            continue
        stats["path_ok"] += 1
        if old_sha.lower() == head.lower():
            stats["already_current"] += 1
            out.append(line)
            continue
        new_body = f"{repo}@{head}:{rel}"
        if symbol:
            new_body += f"#{symbol}"
        # preserve original newline style
        nl = "\n" if line.endswith("\n") else ""
        out.append(f"{prefix}{new_body}{nl}")
        changed = True
        stats["updated"] += 1
    if write and changed:
        path.write_text("".join(out), encoding="utf-8")
        stats["files_written"] += 1
    elif changed:
        stats["files_would_write"] += 1
    return stats


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--repo-root",
        type=Path,
        default=ROOT.parent,
        help="Directory containing sibling git checkouts",
    )
    ap.add_argument("--write", action="store_true", help="Apply SHA updates")
    args = ap.parse_args()

    clones: dict[str, tuple[Path, str]] = {}
    for catalog_id in CLONE_MAP:
        clone = resolve_clone(args.repo_root, catalog_id)
        if clone is None:
            continue
        head = git_head(clone)
        if head:
            clones[catalog_id] = (clone, head)
            # also key by github-style ids used in pointers (often same)
            clones.setdefault(clone.name.replace("-", "_"), (clone, head))

    # Also index by pointer repo names that match clone folder conventions
    extra_alias = {
        "go-radioly-service": "go-radioly",
        "Infra_deployments_k8s": "infra-deployments-k8s",
        "Infra_k8s": "infra-k8s",
        "Novels-Kafka-Stream-Clients": "novels-kafka-stream-client",
    }
    for alias, canon in extra_alias.items():
        if canon in clones and alias not in clones:
            clones[alias] = clones[canon]

    total: Counter = Counter()
    for md in sorted(HANDBOOK.rglob("*.md")):
        if md.name == "README.md":
            continue
        total.update(refresh_file(md, clones, write=args.write))

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Evidence refresh report — {date.today().isoformat()}",
        "",
        f"- mode: `{'write' if args.write else 'dry-run'}`",
        f"- repo_root: `{args.repo_root}`",
        f"- clones_resolved: {len({v[0] for v in clones.values()})}",
        "",
        "## Counts",
        "",
    ]
    for k, v in sorted(total.items()):
        lines.append(f"- **{k}**: {v}")
    lines.append("")
    lines.append("## Clones")
    lines.append("")
    seen: set[Path] = set()
    for cid, (path, head) in sorted(clones.items()):
        if path in seen:
            continue
        seen.add(path)
        lines.append(f"- `{cid}` → `{path.name}` @ `{head[:12]}`")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(REPORT.read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
