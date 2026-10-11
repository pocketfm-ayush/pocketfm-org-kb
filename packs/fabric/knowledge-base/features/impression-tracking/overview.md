# Impression Tracking (Umbrella)

Aliases: fabric impression, frequency counts

Product context: `fabric/pfm-kb/modules/impression-counts.md`

## What it is
Umbrella for Fabric impression platform: Kafka ingest into Scylla time-bucket counts, plus Go/Python query clients used by product services for frequency decisions.

## Graph anchors
| `ImpressionConsumer` | `impression/server/consumer/consumer.go` |
| `clientgo.NewClient` | `impression/clientgo/` |
| `ImpressionClient` | `impression/clientpy/` |

## Risks
- Bypassing clients to query Scylla directly from product services.
- Inventing asset types not on the GTM whitelist.
- Confusing Relay GTM fan-out with Fabric count storage.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "Impression Tracking (Umbrella)" --graph $GRAPH
```
