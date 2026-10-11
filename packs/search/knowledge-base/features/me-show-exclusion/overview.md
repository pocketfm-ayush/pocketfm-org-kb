# ME Show Exclusion

Aliases: ME exclusion, mutual exclusion, suppressed show

Product context: `search/pfm-kb/modules/me-show-exclusion.md`

## What it is
Mutual Exclusion (ME): hide shows suppressed for a device across ME groups. Applied on
search result lists for both v2 and v3.

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `MEShowExclusionService` | `v2/search/services/me_show_exclusion_service.py` L20 | 6 | 31 |
| Repos / device state | `device_exclusion_state_repository.py` | 40 | — |

## Key edges
- Imported by `v2/search/views.py` and `v3/search/views.py` [EXTRACTED]
- Called from `universal_search()`, `search_show()`, `search_user()` [EXTRACTED]
- Wired in v3 via `._initialize_services()` / Handler [EXTRACTED/INFERRED]

## Tests
- `v2/search/tests/test_me_show_exclusion_bdd.py`
- `v2/search/tests/test_me_show_exclusion_service.py`
- `v3/search/tests/test_v3_me_override_modules.py` (ME + override on modules)

## Risks
- Cache of suppressed IDs per device — stale cache = wrong visibility.
- Must remain applied after personalization (AI/PGC, campaign) mutates the list.

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "MEShowExclusionService" --graph $GRAPH
```
