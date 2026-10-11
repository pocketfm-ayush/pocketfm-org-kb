# LightRAG (query process) — not hosted inside Groot (this phase)

Org-kb in this repo is Git SoT. LightRAG is a **separate process** that serves
`POST /query` over a projection of org-handbook.

Groot only needs:

```bash
GROOT_ORG_HANDBOOK_ENABLED=true
LIGHTRAG_QUERY_URL=http://127.0.0.1:9621   # or your QA URL
LIGHTRAG_QUERY_TOKEN=                      # if auth enabled
```

## Quality gate (local)

Before calling Lane A "up to mark":

```bash
python org-handbook/scripts/validate_org_kb.py
python org-handbook/scripts/audit_org_kb_evidence.py --check-clones
python org-handbook/lightrag/sync_projection.py --promote
python org-handbook/lightrag/local_query_server.py --port 9621   # separate terminal
python org-handbook/lightrag/smoke_query.py --base-url http://127.0.0.1:9621
python org-handbook/scripts/run_p0_gold_suite.py --base-url http://127.0.0.1:9621
```

`smoke_query.py` asserts the Groot HTTP contract: `/health`, `/query` with
`data.entities[].file_path` evidence pointers and scores ≥ 0.35.

## Local (recommended first)

1. Distill entities under `org-handbook/repositories/` and pass validate + audit.
2. Build projection slot (records manifest; no remote tokens):

```bash
python org-handbook/lightrag/sync_projection.py --promote
```

3. Start the local LightRAG-shaped query process (hybrid keyword + TF-IDF
   vector rank over Git SoT):

```bash
python org-handbook/lightrag/local_query_server.py --port 9621
```

Ranking is hybrid (token overlap + TF-IDF cosine). Entity responses always
include catalog ``repository`` so Groot owns ads/ugc correctly even when
evidence pointers cite Infra_/airflow.

## Real vector LightRAG (optional upgrade)

Local hybrid keyword + TF-IDF (`local_query_server.py`) is the Org Handbook
query process for this phase. **Do not point Groot at cerebro’s arcade-qa
LightRAG** (`…/api/cerebro/lightrag`) — that is a different index
(cerebro-knowledge), not `org-handbook/`.

When you host *this* projection in QA, prefer the **in-process** route on the
existing Groot host (no separate LightRAG deploy):

```bash
GROOT_ORG_HANDBOOK_ENABLED=true
# empty URL → Groot reads org-handbook/ from synced content-knowledge-base
LIGHTRAG_QUERY_URL=
# or explicit (same host):
# LIGHTRAG_QUERY_URL=https://groot.pocketfm-qa.com/org-handbook
```

Groot serves ``GET /org-handbook/health`` and ``POST /org-handbook/query``.

Keep evidence pointers and catalog ``repository`` in the projection — Groot
prefers ``repository`` over the evidence-pointer repo prefix.

4. Health: `curl -s http://127.0.0.1:9621/health`  # local_query_server
   or `curl -s https://groot.pocketfm-qa.com/org-handbook/health`
5. Query smoke: `python org-handbook/lightrag/smoke_query.py`

Full graph LightRAG (team `cerebro-knowledge` `make lightrag-server` or
upstream) can replace this process later; keep the same URL/env contract.
Hits must still expose evidence pointers in `file_path` / references.

## With Groot later

Optional: run LightRAG as a sidecar next to Groot. **Not required now.**
Keep Groot as an HTTP client until then.

## Safe sync

Publish to a **next** index slot → smoke → promote to **live**. Never upsert
live mid-flight while Groot is querying. `sync_projection.py` writes
`slots/next` then `--promote` copies to `slots/live`.
