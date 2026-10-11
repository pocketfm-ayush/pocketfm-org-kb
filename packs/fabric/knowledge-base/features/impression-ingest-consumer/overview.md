# Impression Ingest Consumer

Aliases: impression server -mode=consumer, GTM/ADS impression Kafka

Product context: `fabric/pfm-kb/modules/impression-ingest.md`

## What it is
Impression server Kafka consumer that accepts GTM and ADS impression events (device/user/retry), validates, and writes frequency-scoped counts.

## Graph anchors
| `Start()` | `impression/server/consumer/bootstrap.go` |
| `ProcessEvent` | `impression/server/consumer/consumer.go` |
| `main -mode=consumer` | `impression/server/cmd/main.go` |

## Risks
- Assuming HTTP API ingest — this path is Kafka consumer mode.
- Dropping retries without understanding GTM_RETRY_IMPRESSION path.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "Impression Ingest Consumer" --graph $GRAPH
```
