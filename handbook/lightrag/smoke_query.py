#!/usr/bin/env python3
"""Smoke LightRAG-shaped /query for Groot Lane A contract.

Checks:
  - GET /health ok
  - POST /query returns response + data.entities with file_path pointers
  - At least one entity score >= 0.35
  - Evidence pointer parses (repo@sha:path#symbol)

Usage:
  python org-handbook/lightrag/smoke_query.py --base-url http://127.0.0.1:9621
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request

PTR = re.compile(
    r"^[A-Za-z0-9_.-]+@[0-9a-fA-F]{7,40}:[^#]+(?:#[A-Za-z0-9_.-]+)?$"
)


def _require_http_url(url: str) -> None:
    if not url.startswith(("http://", "https://")):
        raise ValueError(
            f"URL must start with http:// or https://, got: {url!r}"
        )


def get(url: str) -> dict:
    _require_http_url(url)
    with urllib.request.urlopen(url, timeout=5) as resp:
        return json.loads(resp.read().decode())


def post(url: str, payload: dict) -> dict:
    _require_http_url(url)
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read().decode())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:9621")
    parser.add_argument(
        "--query",
        default="Continue Playing module radioly_client_api resume pointer",
    )
    args = parser.parse_args()
    base = args.base_url.rstrip("/")
    errors: list[str] = []

    health = get(f"{base}/health")
    if health.get("status") != "ok":
        errors.append(f"health not ok: {health}")
    if int(health.get("entities") or 0) < 1:
        errors.append("health reports 0 entities")

    body = post(
        f"{base}/query",
        {"query": args.query, "mode": "hybrid", "top_k": 8, "include_references": True},
    )
    if not isinstance(body.get("response"), str):
        errors.append("missing string response")
    data = body.get("data")
    if not isinstance(data, dict):
        errors.append("missing data object")
        data = {}
    entities = data.get("entities") or []
    if not entities:
        errors.append("no entities returned")
    confident = 0
    ptr_ok = 0
    for ent in entities:
        if not isinstance(ent, dict):
            errors.append(f"bad entity: {ent!r}")
            continue
        score = float(ent.get("score") or 0)
        if score >= 0.35:
            confident += 1
        fp = str(ent.get("file_path") or "")
        if PTR.match(fp):
            ptr_ok += 1
        elif "@" in fp:
            errors.append(f"file_path not a valid evidence pointer: {fp}")
    if confident < 1:
        errors.append("no entity with score >= 0.35")
    if ptr_ok < 1:
        errors.append("no entity with parseable evidence pointer in file_path")

    if errors:
        print("FAIL smoke_query:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(
        f"OK smoke: entities={len(entities)} confident>={confident} "
        f"pointers={ptr_ok} health_entities={health.get('entities')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
