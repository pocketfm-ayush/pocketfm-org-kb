# Continue Playing Candidates

Aliases: continue-playing/shows, CP ranking

Product context: `content-backend/pfm-kb/modules/home-continue-playing-slices.md`

## What it is
Ranks onboarding and recently played shows into active/stale Continue Playing candidates for home/experience callers.

## Graph anchors
| `NewService()` | `internal/app/continueplaying/service.go` |
| `GetCandidates` | `internal/app/continueplaying/controller.go` |

## Risks
- Ignoring geo-restricted show filtering.
- Treating stale vs active thresholds as product copy without reading service constants.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "NewService()" --graph $GRAPH
```
