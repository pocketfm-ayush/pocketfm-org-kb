# Event Config Admin API

Aliases: private /pvt/config CRUD

Product context: `go-radioly-service/pfm-kb/modules/event-config-admin.md`

## What it is
Private HTTP APIs to list/create/update event allowlist/routing config consumed by workers after cache refresh.

## Graph anchors
| `GetAllConfigs` | `internal/gateway/http/routes.go` |
| `CreateConfig` | `internal/gateway/http/routes.go` |

## Risks
- Exposing /pvt without network policy.
- Expecting instant global effect before cache refresh window.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "GetAllConfigs" --graph $GRAPH
```
