# FastPass Story Release

Aliases: fastpass domain feature

Product context: `content-backend/pfm-kb/modules/fastpass-story-release.md`

## What it is
Domain rule that can hide earlier stories / reshape natural sequence based on FastPass release state for eligible shows.

## Graph anchors
| `Apply` | `internal/domain/features/fastpass/fastpass.go` |
| `GetStories` | `internal/domain/stories/service.go` |

## Risks
- Changing story order without validating FastPass lookback and legacy last-story maps.
- Treating FastPass as a payments entitlement API — it is catalog shaping here.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "Apply" --graph $GRAPH
```
