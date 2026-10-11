# Event Relay Pipeline

Aliases: relay service, go-radioly-service umbrella

Product context: `go-radioly-service/pfm-kb/modules/event-relay.md`

## What it is
Umbrella for Relay: client/backend events enter, route by tenant, and export S2S to growth platforms.

## Graph anchors
| `main()` | `cmd/main.go` |
| `InitInfra()` | `internal/bootstrap/base.go` |

## Risks
- Confusing ownership with kafka-stream-clients S2S workers for the same event name.
- Assuming one binary mode covers all paths.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "main()" --graph $GRAPH
```
