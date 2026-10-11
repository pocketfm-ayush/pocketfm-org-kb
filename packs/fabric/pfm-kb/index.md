# Fabric (platform)

Impression counts for frequency decisions, playtime consumers for feed-show
exclusion and AI↔PGC progress sync, plus Temporal namespace YAML (ops-only).

**Modules**

- [impression-counts](modules/impression-counts.md)
- [impression-ingest](modules/impression-ingest.md)
- [gtm-asset-whitelist](modules/gtm-asset-whitelist.md)
- [ads-impression-counts](modules/ads-impression-counts.md)
- [impression-go-client](modules/impression-go-client.md)
- [impression-python-client](modules/impression-python-client.md)
- [playtime-tracking](modules/playtime-tracking.md)
- [audio-playtime-ingest](modules/audio-playtime-ingest.md)
- [feed-show-exclusion](modules/feed-show-exclusion.md)
- [ai-pgc-playtime-sync](modules/ai-pgc-playtime-sync.md)
- [playtime-content-client](modules/playtime-content-client.md)
- [temporal-namespaces](modules/temporal-namespaces.md)

**Flows**

- [feed-show-exclusion-threshold-breach](flows/feed-show-exclusion-threshold-breach.md)
- [impression-event-to-count-query](flows/impression-event-to-count-query.md)
- [ai-pgc-progress-sync](flows/ai-pgc-progress-sync.md)

Related: `radioly` (caps callers, AI↔PGC selection), `kafka-stream-clients`
(audio playtime workers), `go-radioly-service` (GTM impression fan-out),
`airflow` (Temporal workflows — not namespaces).
