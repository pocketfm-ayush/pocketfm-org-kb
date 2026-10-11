# Fabric — service map

| Component | Mode / surface | Product twins |
|---|---|---|
| impression server | `-mode=consumer` | impression-ingest, gtm-asset-whitelist, ads-impression-counts |
| impression clients | library | impression-go-client, impression-python-client |
| playtime | `consumer-playtime` | audio-playtime-ingest (verify incomplete) |
| playtime | `consumer-feed-show-exclusion` | feed-show-exclusion, playtime-content-client |
| playtime | `consumer-ai-pgc-sync` | ai-pgc-playtime-sync |
| temporal-namespaces | YAML + CI sync | temporal-namespaces (ops) |

Downstream services query impression via clients; do not bypass to Scylla.
Radioly listening progress and kafka playtime workers are separate packs.
