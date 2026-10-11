# Handbook schema

Canonical **meaning + evidence** for Pocket FM services (Lane A).

## catalog.yaml

```yaml
version: 1
repos:
  <repository_id>:
    github: Pocket-Fm/<name>
    wave: P0|P1|P2|P3
    status: pending|ready|blocked
    groot_pack: <optional pack folder in content-knowledge-base>
    notes: optional
```

- `repository_id` must match folder `repositories/<repository_id>/`.
- `status: ready` requires ≥1 entity file and a passing `make validate`.
- Prefer `blocked` + notes when the GitHub name is wrong.

## Entity file

Path: `repositories/<repository_id>/<type>/<canonical_id>.md`

```yaml
---
id: flow.unlock-show
type: flow          # flow|interface|capability|service|module
repository: radioly_client_api
status: established # established|uncertain|deprecated
evidence:
  - radioly_client_api@<40hex>:<path>#<symbol>
---
```

Body: short meaning (what / when / ownership). Relationships only when
evidence-backed.

### Evidence quality bar

1. Full **40-char** commit SHA
2. Path must exist at that SHA
3. Symbol required for source files (`.py`, `.go`, `.kt`, `.swift`, …)
4. Prefer `uncertain` over inventing ownership

## Validation

```bash
make validate
# or: python scripts/validate_handbook.py
```
