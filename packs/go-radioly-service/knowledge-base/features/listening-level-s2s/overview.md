# Listening Level S2S Fan-out

Aliases: S2SLevelHandler, hours_listened, level_achieved

Product context: `go-radioly-service/pfm-kb/modules/listening-level-s2s.md`

## What it is
Router handler that expands listening progress / level milestones into device+user S2S event names for platform export.

## Graph anchors
| `S2SLevelHandler` | `internal/eventrouter/handlers/s2s_level.go` |

## Risks
- Hard-coding hour/day thresholds without reading handler interval logic.
- Assuming comics and FM share identical level event naming.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "S2SLevelHandler" --graph $GRAPH
```
