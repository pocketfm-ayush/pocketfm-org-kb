# User attribution to Meta

## Journey
1. Client stores fbp/fbc (or related) via user attribution API.
2. Later purchase/registration event hits Meta exporter.
3. If payload lacks cookies, exporter resolves them from attribution store.
4. IAM/Nexus/IP/Payments enrichment may attach hashed user/value fields.
5. Meta CAPI receives the enriched event.

## Modules
- [user-attribution](../modules/user-attribution.md)
- [export-meta](../modules/export-meta.md)
- [event-enrichment](../modules/event-enrichment.md)

## Failure modes
- Missing attribution row → Meta event without cookie fields.
- Enrichment dependency outage → degraded but possibly still sent payload.
