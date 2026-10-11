# Audiobook Feed Modules

Aliases: get_feed_data, audiobook modules

Product context: `content-backend/pfm-kb/modules/audiobook-feed.md`

## What it is
Authenticated app route that builds audiobook feed modules (popular/trending style) by joining module config with show catalog.

## Graph anchors
| `NewService()` | `internal/app/feed/service.go` |
| `GetFeedData` | `internal/app/feed/controller.go` |

## Risks
- Assuming this is the full home feed — it is audiobook-module oriented.
- Hard-coding module display names without checking rename maps.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "NewService()" --graph $GRAPH
```
