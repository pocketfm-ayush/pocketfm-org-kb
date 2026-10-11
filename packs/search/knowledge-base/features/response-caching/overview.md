# Response Caching

Aliases: search cache, cache hit, cache miss

Product context: `search/pfm-kb/modules/response-caching.md`

## What it is
Redis-backed response cache for universal search: key construction, compress/decompress,
cache-hit personalization (store AI+PGC candidates, personalize per user), and
`redis_except()` degradation when Redis is down.

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `RedisUtils` | `v2/radioly_api/redis_utils.py` L28 | 3 | 124 (god node) |
| `redis_except()` | same area | 3 | 62 |
| `get_universal_search_cache_key()` | `v2/search/cache_key_utils.py` | 0 | — |
| `cache_search_response()` | `v2/search/services/search_response_service.py` | 0 | — |

## Key edges
- `RedisUtils` bridges many communities (report: high betweenness) — almost every feature
  touches it.
- Handler personalizes cache hits differently from misses (Community 14).
- GRAPH_REPORT asks to verify ~23 INFERRED edges on `RedisUtils`.

## Tests
- Cache hit/miss scenarios in `test_universal_search_endpoint_bdd.py`,
  `test_v3_universal_search_bdd.py` (`src_v3:` prefix)

## Risks
- **#1 Search bug class:** response shape change without cache-key change.
- Redis-down path must return usable results (`redis_except`).
- Sharded keys / compression TODOs live in Community 23.

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "RedisUtils" --graph $GRAPH
graphify explain "get_universal_search_cache_key" --graph $GRAPH
```
