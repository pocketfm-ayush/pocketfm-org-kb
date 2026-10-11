# Architecture — Pocket FM Org KB instance

## Split

```text
┌─────────────────────────────────────────────────────────┐
│  org-kb master (engine)                                 │
│  parsers · connectors · indexes · query · eval · UI     │
└───────────────────────────┬─────────────────────────────┘
                            │ ORG_BRAIN_INSTANCE
                            ▼
┌─────────────────────────────────────────────────────────┐
│  pocketfm-org-kb (this repo)                            │
│  org.yaml · policies · handbook · memory · evaluation   │
└───────┬─────────────────────┬───────────────────────────┘
        │                     │
        ▼                     ▼
┌──────────────────┐  ┌──────────────────┐
│ content-kb packs │  │ cerebro-knowledge│
│ (Groot runtime)  │  │ (cross-repo)     │
└────────┬─────────┘  └────────┬─────────┘
         │                     │
         └──────────┬──────────┘
                    ▼
              ┌──────────┐
              │  Groot   │
              └──────────┘
```

## Data flow (target)

1. **Configure** — edit `org.yaml` / catalog / policies in this repo
2. **Bootstrap** — engine inventories sources → Postgres knowledge version
3. **Distill** — handbook entities written with evidence pointers
4. **Sync peers** — optional import from CKB packs + Cerebro merged graph
5. **Query** — API / mind map / Groot locate consumes published version
6. **Evaluate** — golden questions gate domain readiness
7. **Remember** — humans add incidents / ADRs / lessons under `memory/`

## Trust ranking (highest → lowest)

1. Source at pinned SHA (code / schema)
2. Handbook entity with valid evidence pointer
3. CKB CONTRACT / features / pfm-kb (pack-scoped)
4. Cerebro reconciled relationships
5. Memory notes (human; may be stale — label dates)
6. Live ops (Sherlock) — ephemeral, not durable fact
7. Model inference — never published as verified

## Security

- Default profile `repository_read` (no ops write)
- Secrets redacted; never in handbook or memory examples
- Infra repos: docs-safe paths only
- Destructive actions disabled in `org.yaml`
