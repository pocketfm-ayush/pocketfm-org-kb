# Show Details Fallback

Aliases: show_details_fallback compatibility

Product context: `content-backend/pfm-kb/modules/show-details-fallback.md`

## What it is
Compatibility payload for callers that still need a legacy-shaped show details response when primary catalog paths are insufficient.

## Graph anchors
| `NewService()` | `internal/app/showdetailsfallback/service.go` |
| `NewShowDetailsFallbackRepository()` | `internal/repository/show_details_fallback.go` |

## Risks
- Using fallback as the primary catalog path for new features.
- Diverging field meanings from Radioly legacy without checking consumers.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "NewService()" --graph $GRAPH
```
