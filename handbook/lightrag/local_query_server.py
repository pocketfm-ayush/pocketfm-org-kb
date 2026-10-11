#!/usr/bin/env python3
"""Local Org Handbook projection query server (LightRAG-shaped).

Loads org-handbook entity markdown into memory and serves:
  GET  /health
  POST /query
  POST /query/data
  POST /reload

Compatible with Groot ``groot.integrations.lightrag.query``.

Ranking (hybrid keyword + TF-IDF vector):
  - Token overlap with IDF-weighted cosine (improves top-1 vs soft keyword)
  - Prefer ``established`` over ``uncertain``
  - Boost exact catalog repo id tokens and evidence path/symbol tokens
  - Always put a full evidence pointer in ``file_path`` when available
  - Cap scores into [0.35, 1.0] so Groot min-score (default 0.35) can accept hits
  - Response includes ``repository`` (catalog owner) — Groot prefers this over
    evidence-pointer prefix (Infra_/airflow@ cross-repo cites)

Usage (from content-knowledge-base root):
  python org-handbook/lightrag/local_query_server.py --port 9621
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REPOS = ROOT / "repositories"
_FRONT = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)
_TOKEN = re.compile(r"[a-z0-9_./#-]+", re.IGNORECASE)
_STEM_DENY = frozenset(
    {
        "pocket",
        "python",
        "prod",
        "experience",
        "media",
        "infra",
        "client",
        "backend",
        "radio",
        "novels",
        "stream",
        "kafka",
        "go",
        "cms",
        "ios",
        "android",
    }
)


def _parse_entity(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = _FRONT.match(text)
    if not m:
        return None
    meta: dict[str, object] = {}
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
    body = (m.group(2) or "").strip()
    if not meta.get("id"):
        return None
    blob = " ".join(
        [
            str(meta.get("id") or ""),
            str(meta.get("type") or ""),
            str(meta.get("repository") or ""),
            str(meta.get("status") or ""),
            " ".join(evidence),
            body,
            path.as_posix(),
        ]
    ).lower()
    tokens = set(_TOKEN.findall(blob))
    tf: dict[str, float] = {}
    for t in _TOKEN.findall(blob):
        if len(t) < 3:
            continue
        tf[t] = tf.get(t, 0.0) + 1.0
    return {
        "id": str(meta.get("id")),
        "type": str(meta.get("type") or ""),
        "repository": str(meta.get("repository") or ""),
        "status": str(meta.get("status") or "established"),
        "evidence": evidence,
        "body": body,
        "tokens": tokens,
        "tf": tf,
        "path": str(path.relative_to(ROOT)),
    }


def load_index() -> list[dict]:
    entities: list[dict] = []
    if not REPOS.is_dir():
        return entities
    for path in sorted(REPOS.rglob("*.md")):
        if path.name.upper() == "README.MD":
            continue
        ent = _parse_entity(path)
        if ent:
            entities.append(ent)
    return entities


def _build_idf(entities: list[dict]) -> dict[str, float]:
    df: dict[str, int] = {}
    n = max(1, len(entities))
    for ent in entities:
        for t in ent.get("tf") or {}:
            df[t] = df.get(t, 0) + 1
    return {t: math.log((1.0 + n) / (1.0 + c)) + 1.0 for t, c in df.items()}


def _tfidf_vec(tf: dict[str, float], idf: dict[str, float]) -> dict[str, float]:
    return {t: (1.0 + math.log(c)) * idf.get(t, 1.0) for t, c in tf.items() if c > 0}


def _cosine(a: dict[str, float], b: dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    keys = set(a) & set(b)
    if not keys:
        return 0.0
    dot = sum(a[k] * b[k] for k in keys)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na <= 0 or nb <= 0:
        return 0.0
    return dot / (na * nb)


class Index:
    def __init__(self) -> None:
        self.entities = load_index()
        self.idf = _build_idf(self.entities)
        self._vectors = [_tfidf_vec(e.get("tf") or {}, self.idf) for e in self.entities]

    def reload(self) -> None:
        self.entities = load_index()
        self.idf = _build_idf(self.entities)
        self._vectors = [_tfidf_vec(e.get("tf") or {}, self.idf) for e in self.entities]

    def search(self, query: str, top_k: int = 8) -> list[tuple[float, dict]]:
        q_tokens = set(_TOKEN.findall((query or "").lower()))
        q_tokens = {t for t in q_tokens if len(t) >= 3}
        # Split host-like tokens (freshdesk.com → freshdesk) for CS URLs.
        for t in list(q_tokens):
            if "." in t:
                for part in t.split("."):
                    if len(part) >= 3:
                        q_tokens.add(part)
        if not q_tokens:
            return []
        q_tf: dict[str, float] = {}
        for t in q_tokens:
            q_tf[t] = q_tf.get(t, 0.0) + 1.0
        q_vec = _tfidf_vec(q_tf, self.idf)

        scored: list[tuple[float, dict]] = []
        for ent, evec in zip(self.entities, self._vectors):
            overlap = q_tokens & ent["tokens"]
            if not overlap:
                continue
            overlap_score = len(overlap) / max(2.5, len(q_tokens) ** 0.5)
            vec_score = _cosine(q_vec, evec)
            score = 0.55 * overlap_score + 0.55 * vec_score
            repo = (ent["repository"] or "").lower()
            if repo and repo in q_tokens:
                score += 0.45
            repo_stem = repo.split("_")[0].split("-")[0]
            if (
                repo_stem
                and len(repo_stem) >= 5
                and repo_stem not in _STEM_DENY
                and repo_stem in q_tokens
            ):
                score += 0.35
            repo_compact = repo.replace("_", "").replace("-", "")
            if any(t.replace("_", "").replace("-", "") == repo_compact for t in q_tokens):
                score += 0.2
            id_parts = set(re.split(r"[._-]+", (ent["id"] or "").lower()))
            for t in q_tokens:
                # Exact id-segment match only (deny generic stems).
                if len(t) >= 5 and t not in _STEM_DENY and t in id_parts:
                    score += 0.25
                if t in {"fm-ads", "fmads", "ads"} and repo == "ads":
                    score += 0.35
                if t.startswith("ugc") and repo.startswith("ugc"):
                    score += 0.3
            for ptr in ent["evidence"]:
                pl = ptr.lower()
                ptr_body = pl.split(":", 1)[-1]
                for t in q_tokens:
                    if len(t) <= 4:
                        continue
                    if t == "pocketfm" and "/pocketfm/" in ptr_body.replace(".", "/"):
                        continue
                    if t in pl:
                        score += 0.12
            if ent["status"] == "uncertain":
                score *= 0.85
            elif ent["status"] == "deprecated":
                score *= 0.5
            score = min(score, 1.0)
            if score < 0.35:
                continue
            scored.append((score, ent))
        rare_q = {t for t in q_tokens if len(t) >= 6}

        def _tie_key(item: tuple[float, dict]) -> tuple:
            sc, ent = item
            repo = (ent["repository"] or "").lower()
            repo_stem = repo.split("_")[0].split("-")[0]
            exact_repo = any(t == repo or t == repo_stem for t in q_tokens)
            return (
                -sc,
                0 if ent["status"] == "established" else 1,
                -len(rare_q & ent["tokens"]),
                0 if exact_repo else 1,
                ent["id"],
            )

        scored.sort(key=_tie_key)
        return scored[: max(1, min(32, top_k))]


INDEX = Index()


def _response_payload(query: str, top_k: int) -> dict:
    hits = INDEX.search(query, top_k=top_k)
    entities = []
    references = []
    answer_bits = []
    for score, ent in hits:
        ptr = ent["evidence"][0] if ent["evidence"] else ""
        for cand in ent["evidence"]:
            if "#" in cand:
                ptr = cand
                break
        desc = ent["body"][:800]
        if ptr:
            desc = f"{desc}\nEvidence: {ptr}"
        for extra in ent["evidence"][1:3]:
            desc = f"{desc}\nAlso: {extra}"
        entities.append(
            {
                "entity_name": ent["id"],
                "description": desc,
                "file_path": ptr or ent["path"],
                "score": round(score, 4),
                "repository": ent["repository"],
                "status": ent["status"],
            }
        )
        if ptr:
            references.append(
                {
                    "reference_id": ent["id"],
                    "file_path": ptr,
                    "repository": ent["repository"],
                }
            )
        answer_bits.append(
            f"{ent['repository']}: {ent['id']} — {ent['body'][:240]}"
            + (f" [{ptr}]" if ptr else "")
        )
    answer = "\n".join(answer_bits[:5]) if answer_bits else ""
    return {
        "response": answer,
        "data": {"entities": entities, "references": references},
        "references": references,
        "ranking": "hybrid_keyword_tfidf",
    }


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt: str, *args) -> None:
        sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    def _json(self, code: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path.rstrip("/") or "/"
        if path in ("/health", "/"):
            self._json(
                200,
                {
                    "status": "ok",
                    "service": "org-handbook-local-query",
                    "entities": len(INDEX.entities),
                    "ranking": "hybrid_keyword_tfidf",
                    "contract": "groot.integrations.lightrag",
                },
            )
            return
        self._json(404, {"error": "not found"})

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path.rstrip("/") or "/"
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8") or "{}")
        except json.JSONDecodeError:
            self._json(400, {"error": "invalid json"})
            return
        if path == "/reload":
            INDEX.reload()
            self._json(200, {"status": "reloaded", "entities": len(INDEX.entities)})
            return
        if path in ("/query", "/query/data"):
            q = str(payload.get("query") or payload.get("ask") or "")
            top_k = int(payload.get("top_k") or 8)
            self._json(200, _response_payload(q, top_k))
            return
        self._json(404, {"error": "not found"})


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9621)
    args = parser.parse_args()
    if not INDEX.entities:
        print("WARN: no entities loaded from", REPOS, file=sys.stderr)
    else:
        print(f"Loaded {len(INDEX.entities)} entities from {REPOS}", file=sys.stderr)
        print("Ranking: hybrid keyword + TF-IDF cosine", file=sys.stderr)
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    print(f"Listening on http://{args.host}:{args.port}", file=sys.stderr)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nbye", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
