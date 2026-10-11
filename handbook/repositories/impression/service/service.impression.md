---
id: service.impression
type: service
repository: impression
status: uncertain
evidence:
  - fabric@56264ee2c9fc7d8141e98cf5a3ef0c9fc25178d1:impression/server/cmd/main.go#main
  - fabric@56264ee2c9fc7d8141e98cf5a3ef0c9fc25178d1:impression/server/consumer/consumer.go#ProcessEvent
---

Kafka impression aggregator currently lives under `fabric/impression/` (no
standalone Pocket-Fm/impression GitHub). Consumer server + Scylla clients for
user/device impression counts.
