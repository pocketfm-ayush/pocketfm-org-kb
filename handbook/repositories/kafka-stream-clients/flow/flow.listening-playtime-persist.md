---
id: flow.listening-playtime-persist
type: flow
repository: kafka-stream-clients
status: established
evidence:
  - kafka-stream-clients@84a90c1797a9b6711c25e142c7f4b604f8b49c1c:workers/streaming/audio_playtime.py#UpsertDataInCassandra
  - kafka-stream-clients@84a90c1797a9b6711c25e142c7f4b604f8b49c1c:workers/streaming/audio_playtime.py#AudioPlaytimeConsumer
---

Critical pipeline writes user/device story playtime into Scylla via
`UpsertDataInCassandra` / `AudioPlaytimeConsumer`. Request path can ACK before
this finishes.
