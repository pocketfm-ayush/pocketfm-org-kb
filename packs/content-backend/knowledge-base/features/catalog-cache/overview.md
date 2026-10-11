# Catalog Cache & Warmup

Aliases: WithCache, cache invalidation, cache-warmup

Product context: `content-backend/pfm-kb/modules/catalog-cache.md`

## What it is
Two-tier in-memory + Valkey caching for catalog reads, private cache invalidation, and warmup status for hot show ids.

## Graph anchors
| `WithCache` | `internal/cache/wrapper.go` |
| `NewManager()` | `internal/cachewarmup/manager.go` |
| `InvalidateShowCaches` | `internal/app/show/controller.go` |
| `startCacheInvalidationSubscriber` | `internal/bootstrap/apiserver/cache_invalidation_subscriber.go` |

## Risks
- Letting Redis errors fail the user request — writes are best-effort.
- Using MGET across slots instead of pipelined GETs.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "WithCache" --graph $GRAPH
```
