# Org Handbook (org-kb)

Canonical **meaning + evidence** for Pocket FM services. System of record for
Lane A (Groot → LightRAG). Packs under `<pack>/knowledge-base/` remain the
legacy path when `GROOT_ORG_HANDBOOK_ENABLED=false`.

## Layout

```text
org-handbook/
  README.md                 # this file
  SCHEMA.md                 # entity + evidence contract
  catalog.yaml              # all target repos + distill status
  repositories/<repo_id>/   # per-repo entities (markdown)
  scripts/validate_org_kb.py
  lightrag/README.md        # how to run query process (separate from Groot)
```

## Create / expand (all repos)

1. Add or update the repo in `catalog.yaml` (`status: pending`).
2. Distill from the app repo at a fixed SHA → write entities under
   `repositories/<repo_id>/` with evidence pointers.
3. Run `python org-handbook/scripts/validate_org_kb.py` (must pass).
4. Set `status: ready` in catalog when validation is green.
5. Open a PR to content-knowledge-base. After merge, sync projection into
   LightRAG (see `lightrag/README.md`) — **next → smoke → promote**; never
   mutate live mid-sync.
6. Groot: `GROOT_ORG_HANDBOOK_ENABLED=true` + `LIGHTRAG_QUERY_URL` pointing at
   that running LightRAG process.

Invoke Cursor skill **pfm-org-handbook** for the distill workflow.

## Evidence pointer (required on every fact)

```text
<repository-id>@<40-char-sha>:<path>#<symbol>
```

Example: `radioly_client_api@abc…def:v3/unlocking/views.py#unlock_show`

Prefer `unknown` over inventing ownership or production state.
