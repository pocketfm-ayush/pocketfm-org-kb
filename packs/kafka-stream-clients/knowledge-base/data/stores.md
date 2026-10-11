# kafka-stream-clients stores

| Store | Role |
|---|---|
| Kafka | Input event bus (MSK and classic clusters) |
| MySQL | Progress, wallet, unlocks, many product tables |
| Redis | Caches / temporary keys (e.g. RV streak keys) |
| Scylla / Cassandra | Ads playtime, unlocks, user-actions, packaged data |
| S3 | Dumps (reactivation, user-actions, packaged deployment) |

Workers must not open live Kafka/MySQL/Redis in unit tests.
