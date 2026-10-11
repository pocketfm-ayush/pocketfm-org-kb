# Repo Mind — content-backend

Skills + orchestrator must obey this file and `contract.json`. Feature detail lives
in `features/` when present; the code graph lives in `../graphify/graphify-out/`.

**GitHub:** https://github.com/Pocket-Fm/content-backend
**Stack:** Go 1.25 · Gin · GORM/MySQL · Scylla · Valkey Redis

## Purpose

Load `content-backend/pfm-kb/` for product meaning (start at `index.md`).

FM consumer content platform: show/story catalog reads, feed helpers, Continue
Playing candidates, AppsFlyer GCD deeplink cache, and compatibility fallbacks.
Controller → service → repository. Radioly remains the BFF for many journeys.

## Architecture map

| Layer | Location | Owns |
|---|---|---|
| cmd | `cmd/content-backend/` | api-server entry |
| HTTP wiring | `internal/bootstrap/apiserver/` | composition root, middleware, routes |
| app | `internal/app/` | show, feed, CP, fallback, AppsFlyer GCD |
| domain | `internal/domain/` | stories/shows + features/experiments |
| repository | `internal/repository/` | GORM / adapters |
| cache | `internal/cache/`, `cachewarmup/` | two-tier cache + warmup |

Query the graph before inventing structure:

```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify query "<question>" --graph $GRAPH
graphify explain "<symbol>" --graph $GRAPH
graphify path "<A>" "<B>" --graph $GRAPH
```

## Conventions

- New domain: subpackage under internal/app/, wire in app.NewController and routes.go, then make gen-swagger.
- Never write JSON from a service or repository; return errs.Error.
- Redis/cache writes are best-effort — must not fail the request.
- CODEOWNERS: @Pocket-Fm/content-backend.

## Allowed vs protected paths

See `contract.json` → `allowed_edit_paths` / `protected_paths`.
Never write knowledge-base, graphify, env, or secret files.

## External systems & mocking

mysql, scylla, redis/valkey, apollo media (URL resolve).
Use sqlmock / testutil.ExecuteHTTPRequest. Redis must not fail a request (cache writes are best-effort).

## Commands

```bash
make test
make lint
```

## Rebuild graph

```bash
graphify extract <local-clone> --code-only --out content-backend/graphify
graphify cluster-only content-backend/graphify --no-label
```

## Product context

Catalog product meaning: `content-backend/pfm-kb/` (start at `index.md`).
Code twins: `features/*/overview.md`. Radioly remains the consumer BFF for many journeys.

## Coverage

Inventory: `knowledge-base/coverage.md` · folder map: `architecture/source-folder-map.md`.
~19 feature/`pfm-kb` twins (APIs + domain features/experiments).

## Gaps

- Endpoint-by-endpoint cutover matrix vs Radioly is incomplete — verify routes before claiming migration done.
- Not every `.go` file has a twin (dto/test/infra intentional thin).
- Live experiment allocation % and CMS feed payloads are not packed.
