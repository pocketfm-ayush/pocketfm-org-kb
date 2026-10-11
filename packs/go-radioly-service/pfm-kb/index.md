# Relay (go-radioly-service)

Central event ingest, tenant routing, and S2S export to growth/analytics
platforms across Pocket FM / Comics / Novels / TV.

**Modules**

- [event-relay](modules/event-relay.md)
- [event-ingest](modules/event-ingest.md)
- [tenant-routing](modules/tenant-routing.md)
- [platform-export](modules/platform-export.md)
- [delivery-resilience](modules/delivery-resilience.md)
- [allowlist-event-config](modules/allowlist-event-config.md)
- [export-tiktok](modules/export-tiktok.md)
- [export-firebase](modules/export-firebase.md)
- [export-appsflyer](modules/export-appsflyer.md)
- [export-meta](modules/export-meta.md)
- [export-moengage](modules/export-moengage.md)
- [user-attribution](modules/user-attribution.md)
- [gtm-impression-routing](modules/gtm-impression-routing.md)
- [listening-level-s2s](modules/listening-level-s2s.md)
- [limited-experience-signals](modules/limited-experience-signals.md)
- [event-enrichment](modules/event-enrichment.md)
- [backend-direct-path](modules/backend-direct-path.md)
- [stream-analytics](modules/stream-analytics.md)
- [alexa-event-ingest](modules/alexa-event-ingest.md)
- [event-config-admin](modules/event-config-admin.md)
- [multi-tenant-apps](modules/multi-tenant-apps.md)

**Flows**

- [client-attribution-event](flows/client-attribution-event.md)
- [backend-direct-to-platform](flows/backend-direct-to-platform.md)
- [impression-gtm-export](flows/impression-gtm-export.md)
- [kafka-fallback-replay](flows/kafka-fallback-replay.md)
- [user-attribution-to-meta](flows/user-attribution-to-meta.md)

Related: `kafka-stream-clients` S2S workers (different ownership per event);
Airflow MoEngage/batch jobs are not this real-time path.
