# Universal Search

Aliases: universal search, search v2, search v3, search endpoint, how search works

Product context: `search/pfm-kb/modules/universal-search.md` · flow `search/pfm-kb/flows/search-request.md`

## What it is
HTTP entry for search: parse request, route (empty / genre / text), orchestrate services,
cache, personalize, return response. Exists in **v2** (`universal_search`) and **v3**
(`UniversalSearchV3View` → `UniversalSearchV3Handler` + `QueryRouter`).

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `UniversalSearchV3Handler` | `v3/search/views.py` L115 | 14 | 51 |
| `QueryRouter` | `v3/search/views.py` L89 | 42 | 18 |
| `UniversalSearchV3View` | `v3/search/views.py` L534 | 87 | — |
| `universal_search()` | `v2/search/views.py` L1179 | 0 | 36 |
| `SearchRequestData` | `v3/search/data/request_data.py` L9 | 36 | — |

## Key edges (verify when changing)
- Handler / router → `APIUserData`, `MEShowExclusionService`, `OverrideShowFilterService`,
  `ShowFilterServiceV3`, `UserDisabledShowRemovalService`, experiments [INFERRED]
- Handler → `RedisUtils` [INFERRED]
- v3 still personalizes via v2 services (AI/PGC, campaign, thumbnails)

## Tests
- `v3/search/tests/test_v3_universal_search_bdd.py`
- `v2/search/tests/test_universal_search_endpoint_bdd.py`
- `v2/search/tests/test_user_experience_bdd.py`

## Risks
- Cache key must change if response shape changes (`src_v3:` prefix on v3).
- Blast radius spans almost every Search feature — treat as the composition root.
- v2/v3 parity: behavior changes often need both endpoints.

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "UniversalSearchV3Handler" --graph $GRAPH
graphify path "UniversalSearchV3Handler" "ShowSearchServiceV3" --graph $GRAPH
```
