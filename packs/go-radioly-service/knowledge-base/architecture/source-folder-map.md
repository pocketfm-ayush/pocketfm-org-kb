# Relay source folder map

| Folder | Product meaning |
|---|---|
| `internal/gateway/` | HTTP ingest, validation, attribution APIs, stream analytics |
| `internal/eventrouter/` | Tenant fan-out + specialized impression/level handlers |
| `internal/exporter/` | S2S providers + whitelist/dedup/error handling |
| `internal/fallback/` | Gateway Kafka failure buffer + S3 replay |
| `internal/eventconfig/` | Allowlist/routing config cache |
| `internal/externalservices/` | IAM, Nexus, Payments, IPAPI, AppsFlyer helpers |
| `internal/bootstrap/` | Per-mode process startup |
| `internal/repository/` | Scylla/MySQL access for config + attribution + users |
| `cmd/` | Mode selection entrypoint |

Query graph before inventing new packages.
