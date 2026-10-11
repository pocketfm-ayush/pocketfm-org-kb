# Relay — service map

| Mode | Role | Product twins |
|---|---|---|
| Gateway | HTTP ingest; batch always ACK; per-event DLQ | event-ingest, stream-analytics, alexa-event-ingest, user-attribution, event-config-admin |
| Event router | Fan-out + GTM/level handlers | tenant-routing, gtm-impression-routing, listening-level-s2s, limited-experience-signals, multi-tenant-apps |
| Exporter-* | S2S delivery | platform-export, export-tiktok/firebase/appsflyer/meta/moengage, event-enrichment |
| Fallback-replay | S3 → Kafka replay | delivery-resilience |

Backend-direct Kafka path can bypass gateway/router and still hit exporters (`backend-direct-path`).
Allowlist/routing config is DB-driven with periodic refresh (`allowlist-event-config`).
