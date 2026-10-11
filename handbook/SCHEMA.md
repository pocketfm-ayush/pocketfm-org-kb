# Org Handbook schema

## catalog.yaml

```yaml
version: 1
repos:
  <repository_id>:
    github: Pocket-Fm/<name>
    wave: P0|P1|P2|P3
    status: pending|ready|blocked
    notes: optional
```

- `repository_id` must match folder `repositories/<repository_id>/`.
- `status: ready` requires at least one entity file and a passing validate.
- Prefer `blocked` + notes when the GitHub name is wrong or code lives elsewhere.

## Entity file

Path: `repositories/<repository_id>/<type>/<canonical_id>.md`

YAML frontmatter (required):

```yaml
---
id: flow.unlock-show          # stable canonical_id; filename must match
type: flow                    # flow|interface|capability|service|…
repository: radioly_client_api
status: established           # established|uncertain|deprecated
evidence:
  - radioly_client_api@<40hex>:<path>#<symbol>
---
```

Body: short meaning (what / when / ownership). Relationships only when
evidence-backed. Prefer `uncertain` over inventing ownership.

### Locator body conventions (optional, recommended)

Put these in the markdown body (frontmatter keys optional; validate does not
require them yet):

- **Aliases** — alert titles, channel names, product synonyms (`[PROD][FM-ADS]`,
  `#tech-cs-issues`, “ads not loading”).
- **When to use** — first-stop triage vs sibling repos.
- **Required inputs** — VOC / Freshdesk body, UID+symptom, alert service name.
  If missing → ask for data points; do **not** multi-repo code-search.

### Evidence quality bar

1. **SHA** — full **40-char** commit SHA (immutable).
2. **Path** — must exist at that SHA in the owning Git repo.
3. **Symbol** — required for source files (`*.py`, `*.go`, `*.kt`, `*.swift`, …).
   Shell/config/docs suffixes (`.sh`, `.yml`, `.md`, …) may omit `#symbol`.
4. **Pointer repo** — usually equals catalog `repository_id`. Cross-repo
   pointers (e.g. `fabric@…` for catalog `impression`) are allowed only when
   catalog `notes` document the real home and entity `status: uncertain`.
5. Avoid README-only evidence for `service.*` entities — cite a real entrypoint.

## Validation

```bash
python org-handbook/scripts/validate_org_kb.py
python org-handbook/scripts/audit_org_kb_evidence.py --check-clones
```

1. `catalog.yaml` parses; every repo has `github`, `wave`, `status`.
2. For `status: ready`: folder exists; ≥1 `*.md` entity; each has `id`,
   `type`, `repository`, `evidence` meeting the quality bar above.
3. `repository` in frontmatter must equal catalog key / folder name.
4. Exit code 0 = pass; non-zero = fail (block merge).
