# Handbook

Canonical **meaning + evidence** for Pocket FM (Lane A / Org Brain).

## Workflow

1. Add or update the repo in `catalog.yaml` (`status: pending`).
2. Distill from the app repo at a fixed SHA → write entities under
   `repositories/<repo_id>/`.
3. Run `make validate`.
4. Set `status: ready` when validation is green.
5. Open a PR. After merge, sync LightRAG / org-brain indexes (never mutate
   live mid-sync).

## Migration from content-knowledge-base

Existing entities live under
`content-knowledge-base/org-handbook/repositories/`. Prefer copying validated
entities here, then keep CKB as a thin pointer or deprecate the nested path
once Groot reads `ORG_BRAIN_INSTANCE` / this handbook.

## Example entity

See `repositories/_example/service/service.example.md` (not a real service —
template only).
