# kafka-stream-clients source folder map

| Folder / script | Product meaning |
|---|---|
| `workers-kafka-critical.sh` | Critical listening playtime deploy |
| `workers-kafka-consumer.sh` | Most product domain consumers |
| `workers-kafka-db-s3.sh` | Coins, feeds dumps, deactivation, user-actions |
| `workers/streaming` | Audio playtime + video impressions |
| `workers/payments` | Coins, recon, mandates, super saver |
| `workers/s2s_events_v2` | Growth S2S + MoEngage |
| `workers/advertisement` | Ads playtime, PAM, response logs |
| `workers/experience` | Reengage, Discover, tropes, shared events |
| `workers/packaged_deployment` | Feed packaging → Redis/S3/Scylla |
| `workers/communication` + `emails` | WhatsApp/email/OTP |
| `utils/` | Shared Kafka/DB helpers |

New worker: add to the correct `workers-kafka-*.sh` as `name,module.path,replicas` (no underscores in name).
