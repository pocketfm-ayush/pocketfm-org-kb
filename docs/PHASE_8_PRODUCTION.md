# Phase 8 — Production hardening (org instance)

Org Brain exit gate: **security + ops acceptance**.

## Security controls (required)

| Control | Where |
|---|---|
| Tenant isolation | `org.yaml` `security.tenant_isolation: required` |
| Secret redaction | `security.redact_secrets: true` |
| Source ACL | `enforce_source_permissions: true` |
| No destructive actions | `allow_destructive_actions: false` |
| Infra docs-safe only | P3 repos notes + indexing excludes |
| Query-time profiles | `policies.yaml` |

Threat model (engine): see org-kb `docs/THREAT_MODEL.md`. Local copy of
mitigations we enforce in this instance:

1. No secrets / `.env` / tokens in handbook, packs, or memory
2. Evidence pointers use immutable SHAs (refresh via `scripts/refresh_evidence_from_clones.py`)
3. Live ops never promoted to durable handbook fact without human distill
4. Partial maps labeled incomplete (`status: uncertain` / catalog `pending|blocked`)

## Operations

```bash
export ORG_BRAIN_INSTANCE="$(pwd)"
make validate
python3 scripts/refresh_evidence_from_clones.py --write   # after pulling app repos
# When engine available:
#   org-brain preflight && org-brain bootstrap
#   org-brain evaluate   # golden + cerebro suites under evaluation/
```

### Backups

- Git: this repo (`handbook/`, `packs/`, `memory/`, `org.yaml`, `policies.yaml`)
- Postgres (engine): `pg_dump` of org DB — not committed here
- Do not back up embeddings/secrets into git (`var/` is gitignored)

### Recovery

Keep last published knowledge version if a new publish fails. Resume bootstrap
via engine `--resume <job-id>`.

## Acceptance checklist

- [x] Full handbook migrated + validated (`make validate`)
- [x] Evidence refreshed against local clone HEADs (see baselines report)
- [x] Groot packs mirrored under `packs/` (no graphify blobs)
- [x] Cerebro domain resources mirrored under `peers/cerebro/`
- [x] Connectors declared; destructive actions off
- [ ] `org-brain bootstrap` green against this instance
- [ ] Eval suite pass rate recorded under `evaluation/baselines/`
- [ ] Sherlock / MCP allowlists approved for prod
