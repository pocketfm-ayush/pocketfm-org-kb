# Story Catalog Read

Aliases: GetShowStories, QueryStories, episode list

Product context: `content-backend/pfm-kb/modules/story-catalog-read.md`

## What it is
Story/episode list reads for a show, applying FastPass, branching, stitching, and related domain rules before response.

## Graph anchors
| `NewStoryService()` | `internal/app/show/story_service.go` |
| `NewService()` | `internal/domain/stories/service.go` |
| `NewStoryRepository()` | `internal/repository/story_repository.go` |

## Risks
- Shipping story order changes without checking FastPass/branching/stitching interactions.
- Hard-coding natural sequence compaction rules in callers.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "NewStoryService()" --graph $GRAPH
```
