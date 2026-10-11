---
name: kafka
description: Kafka producers/consumers, idempotency, lag, and DLQ discipline.
triggers: [kafka, consumer, producer, topic, consumer lag]
intent: implement
priority: 70
---

# Kafka

## Do
- Idempotent consumers; define poison-message / DLQ behavior.
- Explicit serialization contracts; version payloads when breaking.
- Monitor lag, fail rates, and rebalance storms.
- Ordering only where partitions guarantee it.

## Do not
- Assume global order across partitions.
- Block forever on a bad message without a DLQ plan.

## Related
`database-sql`, `performance-review`, `security-review`, `docker`, `kubernetes` as applicable.
