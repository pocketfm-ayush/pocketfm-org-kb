---
id: service.kafka-stream-clients
type: service
repository: kafka-stream-clients
status: established
evidence:
  - kafka-stream-clients@84a90c1797a9b6711c25e142c7f4b604f8b49c1c:workers/streaming/audio_playtime.py#AudioPlaytimeConsumer
  - kafka-stream-clients@84a90c1797a9b6711c25e142c7f4b604f8b49c1c:workers-kafka-critical.sh
---

Async Kafka consumer fleet for Pocket FM. Critical playtime path is
`AudioPlaytimeConsumer`; pod entry scripts list the wider worker set.
