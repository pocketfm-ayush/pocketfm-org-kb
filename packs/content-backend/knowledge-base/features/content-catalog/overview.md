# Content Catalog (Umbrella)

Aliases: content-backend catalog platform

Product context: `content-backend/pfm-kb/modules/content-catalog.md`

## What it is
Umbrella for the emerging FM content catalog service: show/story reads, feed helpers, and compatibility fallbacks used by Radioly and other callers.

## Graph anchors
| `NewController()` | `internal/app/controller.go` |
| `CreateRouter()` | `internal/bootstrap/apiserver/http.go` |

## Risks
- Claiming Radioly journeys are fully cut over without a route-by-route matrix.
- Writing JSON from services/repositories instead of returning typed errors.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "NewController()" --graph $GRAPH
```
