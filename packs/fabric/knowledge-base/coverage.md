# fabric pack coverage

**As of:** 2026-09-07 · **Ticket:** FMF-4712

## Source reality
- Monorepo tops: `impression/`, `playtime/`, `temporal-namespaces/`, `infra/`
- Impression: server consumer + clientgo + clientpy (~GTM/ADS ingest, query SDKs)
- Playtime modes: `consumer-playtime`, `consumer-feed-show-exclusion`, `consumer-ai-pgc-sync`
- Temporal: declarative namespace YAML synced by CI (workflows live elsewhere)
- ~90 Go files (+ Python client)

## Pack counts
| Layer | Count |
|---|---|
| Feature overviews | 12 |
| pfm-kb modules | 12 |
| pfm-kb flows | 3 |

## Folder map (product twin status)

| Source area | Status | Twin(s) |
|---|---|---|
| `impression/server` | covered | impression-ingest, gtm-asset-whitelist, ads-impression-counts, impression-counts |
| `impression/clientgo` | covered | impression-go-client |
| `impression/clientpy` | covered | impression-python-client |
| `playtime/cmd` + `consumer` | covered | playtime-tracking |
| `playtime/audioplaytime` | covered (honest gap) | audio-playtime-ingest |
| `playtime/feedshowexclusion` | covered | feed-show-exclusion |
| `playtime/aipgcsync` | covered | ai-pgc-playtime-sync |
| `playtime/externalservices/content` | covered | playtime-content-client |
| `playtime/repository` | covered via features | exclusion + AI-PGC + playtime repos |
| `temporal-namespaces/` | covered (ops) | temporal-namespaces |
| `infra/`, local docker/CQL | intentional SKIP | local/dev infra |
| `playtime/test`, impression tests | intentional SKIP | harness |

## Intentional SKIP
- Per-DTO / prepared-statement encyclopedia
- Full GTM asset whitelist dump (read code)
- Live Temporal workflow definitions (other repos)
- Invented Scylla table names

## Honest gaps
- `consumer-playtime` core ingest appears incomplete — verify HEAD
- Frequency-cap *callers* live in Radioly/peers, not only Fabric
- Always use clients — do not bypass to Scylla from product services
