# Backend direct to platform

## Journey
1. Backend service publishes an already-shaped event onto an exporter Kafka topic.
2. Exporter consumes, applies provider whitelist/dedup/enrichment.
3. Platform S2S API receives the event.

## Modules
- [backend-direct-path](../modules/backend-direct-path.md)
- [platform-export](../modules/platform-export.md)
- [event-enrichment](../modules/event-enrichment.md)

## Failure modes
- Invalid backend payloads fail in exporter (no gateway validation safety net).
- Router GTM rewrites do not run on this path.
