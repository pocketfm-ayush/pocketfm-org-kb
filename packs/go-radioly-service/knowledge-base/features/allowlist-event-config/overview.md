# Allowlist Event Config

Aliases: eventconfig, gateway_event_config, ConfigProvider

Product context: `go-radioly-service/pfm-kb/modules/allowlist-event-config.md`

## What it is
DB-driven allowlist and routing destinations for events, cached in memory with periodic refresh. Shared by gateway validation and routing decisions.

## Graph anchors
| `NewManager()` | `internal/eventconfig/manager.go` |
| `ConfigProvider` | `internal/eventconfig/interface.go` |
| `EventConfigRepository` | `internal/repository/event_config.go` |

## Risks
- Hard-coding allowlist rules in code or KB instead of reading live config.
- Assuming refresh is instant after admin write.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "NewManager()" --graph $GRAPH
```
