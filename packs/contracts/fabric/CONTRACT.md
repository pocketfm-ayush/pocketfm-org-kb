# Repo Mind — fabric

Skills + orchestrator must obey this file and `contract.json`. Feature detail lives
in `features/` when present; the code graph lives in `../graphify/graphify-out/`.

**GitHub:** https://github.com/Pocket-Fm/fabric
**Stack:** Go 1.24 · Scylla · Kafka · Temporal namespaces (ops)

## Purpose

Load `fabric/pfm-kb/` for product meaning (start at `index.md`).

Platform monorepo: impression tracking (ingest + query clients), playtime
consumers (feed-show exclusion, AI↔PGC sync; core ingest may be incomplete),
and Temporal namespace YAML (ops-only).

## Architecture map

| Layer | Location | Owns |
|---|---|---|
| impression server | `impression/server` | Kafka consumer → Scylla counts |
| impression clients | `impression/clientgo`, `clientpy` | Query SDKs |
| playtime | `playtime/` | Mode-selected Kafka consumers |
| temporal-namespaces | `temporal-namespaces/` | Protected — declarative Temporal config |

Query the graph before inventing structure:

```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "<question>" --graph $GRAPH
graphify explain "<symbol>" --graph $GRAPH
graphify path "<A>" "<B>" --graph $GRAPH
```

## Conventions

- Each service has its own go.mod. `make test` walks impression/server, impression/clientgo, playtime.
- Playtime modes: `consumer-playtime`, `consumer-feed-show-exclusion`, `consumer-ai-pgc-sync`.
- Impression server mode: `consumer`.
- Prefer impression clients — do not bypass to Scylla from product services.
- Local infra from repo root: `make download-deps` then `docker-compose up -d`.
- CODEOWNERS: @Pocket-Fm/platform-leads.

## Allowed vs protected paths

See `contract.json` → `allowed_edit_paths` / `protected_paths`.
Never write knowledge-base, graphify, env, or secret files.

## External systems & mocking

scylla, kafka, mysql (AI-PGC mode), content API (exclusion), temporal (namespace sync only).
Service tests must not require live Scylla unless the service README says so. Prefer mocks.

## Commands

```bash
make test
echo lint per-service
```

## Rebuild graph

```bash
graphify extract <local-clone> --code-only --out fabric/graphify
graphify cluster-only fabric/graphify --no-label
```

## Product context

Platform product meaning: `fabric/pfm-kb/` (start at `index.md`).
Code twins: `features/*/overview.md`. Temporal namespaces remain ops-only
(`architecture/service-map.md`) — not a listener product journey.

## Coverage

Inventory: `knowledge-base/coverage.md` · folder map: `architecture/source-folder-map.md`.
~12 feature/`pfm-kb` twins. Not a per-file encyclopedia.

## Gaps

- Core audio ingest mode (`consumer-playtime`) may still be incomplete — verify before claiming.
- Caller-side frequency cap ownership lives in Radioly and peers, not this pack alone.
- Temporal *workflows* live in airflow/other services — only namespace YAML is here.
