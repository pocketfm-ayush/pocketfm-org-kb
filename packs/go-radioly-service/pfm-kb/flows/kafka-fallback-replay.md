# Kafka fallback replay

## Journey
1. Gateway accepts a batch but Kafka publish fails.
2. Fallback buffers and stores durable copies.
3. `fallback-replay` workers republish onto Kafka.
4. Normal router/exporter path resumes.

## Modules
- [event-ingest](../modules/event-ingest.md)
- [delivery-resilience](../modules/delivery-resilience.md)
- [tenant-routing](../modules/tenant-routing.md)

## Failure modes
- Replay lag → delayed attribution without client errors.
- Fallback does not cover router/exporter publish failures.
