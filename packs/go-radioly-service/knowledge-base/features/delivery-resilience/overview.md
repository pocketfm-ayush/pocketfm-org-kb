# Delivery Resilience (Fallback)

Aliases: fallback-replay, S3 Kafka fallback

Product context: `go-radioly-service/pfm-kb/modules/delivery-resilience.md`

## What it is
When gateway Kafka publish fails, events buffer and land in S3 for later replay so ingest ACK does not equal permanent loss.

## Graph anchors
| `NewReplayer()` | `internal/fallback/replayer.go` |
| `Start()` | `internal/bootstrap/fallback/fallback.go` |

## Risks
- Expecting fallback to cover router/exporter failures — it is gateway publish only.
- Treating S3 lag as user-facing API failure.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "NewReplayer()" --graph $GRAPH
```
