# Tenant Routing (Event Router)

Aliases: event router mode, routeFM, routeComics

Product context: `go-radioly-service/pfm-kb/modules/tenant-routing.md`

## What it is
Kafka consumer that fans gateway events to tenant-specific downstream topics and runs specialized impression/level handlers before export topics.

## Graph anchors
| `EventRouterCtrl` | `internal/eventrouter/router.go` |
| `ProcessEvent()` | `internal/eventrouter/router.go` |
| `Start()` | `internal/bootstrap/event-router/event_router.go` |

## Risks
- AND-ing field conditions — router uses OR logic across conditions.
- Assuming novels/TV share identical FM routing rules.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "EventRouterCtrl" --graph $GRAPH
```
