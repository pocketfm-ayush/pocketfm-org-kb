#!/usr/bin/env python3
"""Build a local projection slot from org-handbook entities (next → promote).

Writes:
  org-handbook/lightrag/slots/next/manifest.json
  org-handbook/lightrag/slots/live/  (copy of next after --promote)

Does not call remote LightRAG (no tokens). Pair with local_query_server.py
which reads repositories/ directly; this script records the sync slot for
humans/CI.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPOS = ROOT / "repositories"
SLOTS = Path(__file__).resolve().parent / "slots"


def _entities() -> list[dict]:
    out = []
    for path in sorted(REPOS.rglob("*.md")):
        if path.name.upper() == "README.MD":
            continue
        text = path.read_text(encoding="utf-8")
        digest = hashlib.sha256(text.encode()).hexdigest()[:16]
        out.append(
            {
                "path": str(path.relative_to(ROOT)),
                "sha256_16": digest,
                "bytes": len(text.encode()),
            }
        )
    return out


def write_slot(name: str) -> Path:
    slot = SLOTS / name
    slot.mkdir(parents=True, exist_ok=True)
    ents = _entities()
    manifest = {
        "slot": name,
        "built_at": datetime.now(timezone.utc).isoformat(),
        "entity_count": len(ents),
        "entities": ents,
    }
    (slot / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return slot


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--promote", action="store_true", help="copy next → live")
    args = parser.parse_args()
    next_slot = write_slot("next")
    print(f"wrote {next_slot / 'manifest.json'} ({json.loads((next_slot/'manifest.json').read_text())['entity_count']} entities)")
    if args.promote:
        live = SLOTS / "live"
        if live.exists():
            shutil.rmtree(live)
        shutil.copytree(next_slot, live)
        print(f"promoted next → {live}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
