# Playtime Tracking (Umbrella)

Aliases: fabric playtime consumers, mode flag

Product context: `fabric/pfm-kb/modules/playtime-tracking.md`

## What it is
Umbrella for Fabric playtime Kafka consumers selected by `-mode`: core playtime ingest, feed-show-exclusion, and AI↔PGC sync.

## Graph anchors
| `ConfigForMode` | `playtime/consumer/registry.go` |
| `consumer.Start` | `playtime/consumer/consumer.go` |
| `main -mode` | `playtime/cmd/main.go` |

## Risks
- Confusing with kafka-stream-clients listening playtime workers.
- Assuming consumer-playtime core ingest is fully implemented.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "Playtime Tracking (Umbrella)" --graph $GRAPH
```
