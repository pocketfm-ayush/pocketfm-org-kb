# Show Catalog Read

Aliases: GetShow, QueryShows, /internal/show

Product context: `content-backend/pfm-kb/modules/show-catalog-read.md`

## What it is
Internal APIs to fetch one show or query many shows with caching and request-scoped personalization.

## Graph anchors
| `NewShowService()` | `internal/app/show/show_service.go` |
| `GetShow` | `internal/app/show/controller.go` |
| `NewShowRepository()` | `internal/repository/show_data_repository.go` |

## Risks
- Bypassing private API auth on /internal show routes.
- Assuming every Radioly show page already calls this service.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "NewShowService()" --graph $GRAPH
```
