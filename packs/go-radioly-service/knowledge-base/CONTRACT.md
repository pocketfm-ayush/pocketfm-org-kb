# Repo Mind — go-radioly-service (Relay)

Skills + orchestrator must obey this file and `contract.json`. Feature detail lives
in `features/` when present; the code graph lives in `../graphify/graphify-out/`.

**GitHub:** https://github.com/Pocket-Fm/go-radioly-service
**Stack:** Go 1.25 · Gin · Kafka · MySQL · Scylla · Redis

## Purpose

Load `go-radioly-service/pfm-kb/` for product meaning (start at `index.md`).

Relay: ingest clickstream/backend events, route via Kafka, export to TikTok,
Firebase/GA4, AppsFlyer, Meta, MoEngage. Dual path: client HTTP gateway→router
or backend-direct Kafka→exporter.

## Architecture map

| Layer | Location | Owns |
|---|---|---|
| gateway | `internal/gateway/, internal/bootstrap/gateway/` | HTTP ingest, attribution, stream analytics, Kafka publish |
| router | `internal/eventrouter/` | Tenant topics + GTM/level handlers |
| exporter | `internal/exporter/` | S2S to ad/analytics platforms |
| fallback | `internal/fallback/` | S3 replay of gateway Kafka publish failures |
| eventconfig | `internal/eventconfig/` | DB allowlist + routing cache |

Query the graph before inventing structure:

```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify query "<question>" --graph $GRAPH
graphify explain "<symbol>" --graph $GRAPH
graphify path "<A>" "<B>" --graph $GRAPH
```

## Conventions

- Modes: gateway, router, exporter-*, fallback-replay. See CLAUDE.md in the repo.
- New exporter: implement Provider, then whitelist + bootstrap deps. Do not assume MySQL+Scylla+Redis for every mode.
- CODEOWNERS: @Pocket-Fm/platform-leads.

## Allowed vs protected paths

See `contract.json` → `allowed_edit_paths` / `protected_paths`.
Never write knowledge-base, graphify, env, or secret files.

## External systems & mocking

kafka, mysql, scylla, redis, s3, tiktok, firebase, appsflyer, meta, moengage,
iam, nexus, payments, ipapi.
Do not call live exporter APIs in unit tests. Gateway batch ingest always returns HTTP 200; per-event failures go to DLQ.

## Commands

```bash
make test
make lint
```

## Rebuild graph

```bash
graphify extract <local-clone> --code-only --out go-radioly-service/graphify
graphify cluster-only go-radioly-service/graphify --no-label
```

## Product context

Relay product meaning: `go-radioly-service/pfm-kb/` (start at `index.md`).
Code twins: `features/*/overview.md`.

## Coverage

Inventory: `knowledge-base/coverage.md` · folder map: `architecture/source-folder-map.md`.
~21 feature/`pfm-kb` twins (modes + providers + specialized router handlers).

## Gaps

- Per-event ownership vs `kafka-stream-clients` S2S workers — confirm in source.
- Allowlist rules are DB-driven — do not invent them in KB.
- Not every `.go` file has a twin (dto/httpclient/test intentional thin).
