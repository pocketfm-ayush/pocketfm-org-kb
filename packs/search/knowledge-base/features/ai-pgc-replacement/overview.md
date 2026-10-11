# AI / PGC Show Replacement

Aliases: AI PGC, AI/PGC, AI<>PGC, AI <-> PGC, PGC replacement, PGC show selection, user_tg pgc, FMF-3783

Product context: `search/pfm-kb/modules/ai-pgc-replacement.md` · flow `radioly/pfm-kb/flows/ai-pgc-across-surfaces.md`

## What it is
Personalization that swaps AI vs PGC show variants in results based on playtime, cold-start,
and marketing pins (`user_tg = pgc_<id>`, FMF-3783). Applied on cache-miss and cache-hit
personalization paths.

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `apply_pgc_show_replacement()` | `v2/search/services/ai_pgc_show_service.py` L751 | 44 | 26 |
| Pair helpers (`_cold_start_pgc_wins`, etc.) | same file | 8, 22 | — |
| Pair map repo | `show_exclusion_override_repository.py` | 21 | — |

## Key edges
- Called from `_finalize_universal_search_response()` (v2) and
  `._apply_personalization_core()` (v3) [EXTRACTED]
- Uses `pgc_wins_for_pair()` [EXTRACTED]
- Kill-switch / availability guards in Communities 22 / 25

## Tests
- `v2/search/tests/test_ai_pgc_show_replacement_bdd.py`
- `v2/search/tests/test_ai_pgc_user_flow_bdd.py`
- `v2/search/tests/test_ai_pgc_dynamic_pairs.py`

## Risks
- Marketing deeplink pins interact with live/availability checks — easy to break cold-start.
- Must run before/with exclusion filters so swapped IDs still respect ME/override/campaign.
- Playtime reads from Scylla — failure modes need safe fallbacks.

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "apply_pgc_show_replacement" --graph $GRAPH
graphify query "how does AI PGC show replacement work?" --graph $GRAPH --budget 4000
```
