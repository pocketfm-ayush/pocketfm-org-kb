# Client attribution event

## Journey
1. App posts an event batch to Relay gateway.
2. Gateway allowlists and publishes to Kafka (or buffers to fallback on publish failure).
3. Router fans out to tenant topics; specialized handlers may rewrite impressions/levels.
4. Exporter enriches and sends S2S to AppsFlyer / TikTok / Firebase / Meta / MoEngage as configured.
5. Growth dashboards and CRM reflect the event when delivery succeeds.

## Modules
- [event-ingest](../modules/event-ingest.md)
- [allowlist-event-config](../modules/allowlist-event-config.md)
- [tenant-routing](../modules/tenant-routing.md)
- [platform-export](../modules/platform-export.md)
- [delivery-resilience](../modules/delivery-resilience.md)

## Failure modes
- Per-event DLQ while batch still ACKs.
- Fallback lag delays platform visibility without failing the app request.
- Unmatched router events never reach exporters.
