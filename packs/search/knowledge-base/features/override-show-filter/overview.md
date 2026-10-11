# Override Show Filter

Aliases: CS override, manual override, preferred version

Product context: `search/pfm-kb/modules/override-show-filter.md`

## What it is
When a user has manual show overrides (often AI↔PGC pairs), hide alternate versions of
overridden shows from search results.

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `OverrideShowFilterService` | `v2/search/services/override_show_filter_service.py` L28 | 31 | 33 |
| `ShowExclusionOverrideRepository` | `v2/search/repositories/show_exclusion_override_repository.py` | 21 | — |

## Key edges
- Service → repository [INFERRED]
- Called from `_finalize_universal_search_response()` and v3 personalization [EXTRACTED]
- AI↔PGC pair map: Redis → MySQL fallback (Community 21)

## Tests
- `v2/search/tests/test_override_show_filter_service.py`
- `v2/search/tests/test_show_exclusion_override_repository.py`
- `v2/search/tests/test_me_show_exclusion_bdd.py` (imports override too)
- `v3/search/tests/test_v3_me_override_modules.py`

## Risks
- Coupled to AI/PGC pair map — pair cache bugs surface as wrong overrides.
- Order vs ME exclusion matters; keep both in the finalize/personalize pipeline.

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "OverrideShowFilterService" --graph $GRAPH
graphify path "OverrideShowFilterService" "ShowExclusionOverrideRepository" --graph $GRAPH
```
