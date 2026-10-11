# Handbook (Lane A)

Canonical **meaning + evidence** for Pocket FM services.

Migrated from `content-knowledge-base/org-handbook/` and refreshed against
local clone HEADs via `scripts/refresh_evidence_from_clones.py`.

## Layout

```text
handbook/
  catalog.yaml           # 31 repos, waves P0–P3
  SCHEMA.md
  repositories/<id>/     # flow|service|capability|interface entities
  scripts/validate_org_kb.py
  lightrag/              # projection helpers (process runs separately)
```

## Validate

```bash
python3 handbook/scripts/validate_org_kb.py
# or: make validate
```

## Update from source

```bash
# 1. git pull sibling app repos
# 2. refresh SHAs where paths still exist
make refresh-evidence
# 3. for new meaning: distill entity at fixed SHA, then validate
```
