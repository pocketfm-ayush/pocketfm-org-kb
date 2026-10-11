# Kafka Workers (Umbrella)

Aliases: kafka consumers, async workers fleet

Product context: `kafka-stream-clients/pfm-kb/modules/kafka-workers.md`

## What it is
Python Kafka consumer fleet. After live APIs return, workers persist listening progress, unlocks, wallet credits, ads streaks, growth S2S, experience, feeds, and account side effects. Deployed via critical / consumer / db-s3 pipelines.

## Graph anchors
| `workers-kafka-critical.sh` | `workers-kafka-critical.sh` |
| `workers-kafka-consumer.sh` | `workers-kafka-consumer.sh` |
| `workers-kafka-db-s3.sh` | `workers-kafka-db-s3.sh` |

## Risks
- Editing worker names with underscores (K8s entry format forbids them).
- Opening live Kafka/MySQL/Redis in unit tests.
- Fixing the wrong pack (Relay exporters vs these workers) for S2S drops.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Kafka Workers (Umbrella)" --graph $GRAPH
```
