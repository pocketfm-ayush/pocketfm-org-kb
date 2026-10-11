# Event Ingest (Gateway)

Aliases: relay gateway, logging_data/log, batch ingest

Product context: `go-radioly-service/pfm-kb/modules/event-ingest.md`

## What it is
HTTP door for event batches. Validates/allowlists and publishes to the relay bus. Batch ACK means accept, not full downstream export success.

## Graph anchors
| `Service` | `internal/gateway/eventlog/service.go` |
| `NewGateway()` | `internal/gateway/http/gateway.go` |
| `LogEvents` | `internal/gateway/eventlog/controller.go` |

## Risks
- Treating HTTP 200 as proof every event reached TikTok/Meta.
- Skipping allowlist/eventconfig before inventing new event names.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "Service" --graph $GRAPH
```
