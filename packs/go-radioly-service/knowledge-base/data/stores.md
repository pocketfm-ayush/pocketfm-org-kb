# Relay stores

| Store | Role |
|---|---|
| Kafka | Primary bus: gateway → router → exporters (also backend-direct → exporters) |
| MySQL / Scylla | Event allowlist/config; user attribution; some enrichment caches — mode-dependent |
| Redis | Opt-in per exporter bootstrap deps |
| S3 | Fallback buffer for failed gateway publishes |

Verify mode bootstrap (`ExporterConfig.Dependencies`) before assuming a store is required.
