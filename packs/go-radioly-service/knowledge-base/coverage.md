# go-radioly-service (Relay) pack coverage

**As of:** 2026-09-07 · **Ticket:** FMF-4712

## Source reality
- ~173 Go files (~111 non-test) under `cmd/` + `internal/`
- Modes: gateway, router, exporter-tiktok/firebase/appsflyer/meta, fallback-replay
- Providers: TikTok, Firebase, AppsFlyer, Facebook(Meta), MoEngage
- Router handlers: KT / player-feed / show-promo impressions, S2S level, limited experience
- Dual path: client HTTP gateway → router → exporter; backend direct → exporter

## Pack counts
| Layer | Count |
|---|---|
| Feature overviews | 21 |
| pfm-kb modules | 21 |
| pfm-kb flows | 5 |

## Folder map (product twin status)

| Source area | Status | Twin(s) |
|---|---|---|
| `cmd/` | covered via umbrella | event-relay |
| `internal/bootstrap/gateway` + `gateway/` | covered | event-ingest, stream-analytics, alexa-event-ingest, user-attribution, event-config-admin |
| `internal/bootstrap/event-router` + `eventrouter/` | covered | tenant-routing, gtm-impression-routing, listening-level-s2s, limited-experience-signals, multi-tenant-apps |
| `internal/bootstrap/exporter` + `exporter/provider/*` | covered | platform-export, export-* |
| `internal/bootstrap/fallback` + `fallback/` | covered | delivery-resilience |
| `internal/eventconfig` + config admin | covered | allowlist-event-config, event-config-admin |
| `internal/externalservices` | covered | event-enrichment |
| `internal/repository` | covered via features | allowlist, user-attribution |
| `internal/kafka`, `metrics`, `config`, `util` | intentional thin | infra/helpers — use CLAUDE + graph |
| `internal/test` | intentional SKIP | test harness, not product |
| `deployment/`, `infra/` | intentional SKIP | deploy manifests |

## Intentional SKIP
- Unit/integration test trees as product modules
- Prometheus metric name encyclopedias
- Live allowlist rows / platform API secrets
- Per-file twins for dto/enum/httpclient helpers

## Honest gaps
- Product family coverage ≠ one overview per `.go` file
- Event ownership vs `kafka-stream-clients` must be confirmed per event
- Always verify mode bootstrap deps before assuming MySQL/Scylla/Redis
