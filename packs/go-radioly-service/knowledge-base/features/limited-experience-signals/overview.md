# Limited Experience Signals

Aliases: LimitedExperienceHandler, limited experience metrics

Product context: `go-radioly-service/pfm-kb/modules/limited-experience-signals.md`

## What it is
Router-side observation of limited-experience API outcomes for ops metrics (does not invent a new user journey by itself).

## Graph anchors
| `LimitedExperienceHandler` | `internal/eventrouter/handlers/limited_experience.go` |

## Risks
- Treating this as a product unlock feature — it is signal/metrics oriented.
- Inventing response-code policies without reading shouldRecord.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "LimitedExperienceHandler" --graph $GRAPH
```
