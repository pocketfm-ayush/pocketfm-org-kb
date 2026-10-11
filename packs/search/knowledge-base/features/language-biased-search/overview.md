# Language-biased Search

Aliases: text search, relevance, fuzzy search, language pool

Product context: `search/pfm-kb/modules/language-biased-search.md`

## What it is
Core relevance path: multi-phase Elasticsearch/OpenSearch over language pools, with
language boost and fuzzy/prefix fallbacks. Powers text search for both v2 and v3.

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `ShowSearchService` | `v2/search/services/show_search.py` L30 | 10 | 58 |
| `lang_biased_results()` | `v2/search/services/lang_biased_search.py` L679 | 10 | 28 |
| `search_stories_shows_user_lan()` | same file L367 | 29 | — |
| `fuzzy_search_result()` | same file | 29 | — |
| `ShowSearchServiceV3` | `v3/search/services/show_search_v3.py` L16 | 42 | — |

## Key edges
- `lang_biased_results()` → `ShowSearchService` [EXTRACTED]
- `ShowSearchServiceV3` → `ShowSearchService` [INFERRED] — v3 is not standalone
- Callers: `v2/search/views.py`, v3 `._fetch_stories()`, discovery/ranking + web-parity tests

## Related communities
- Community 1 — ES fuzzy / locale / English fallback test nodes
- Community 10 — 3-phase ES strategy, ranking
- Community 27 / 32 / 35 — locale language pools, msearch batching tests

## Tests
- `v2/search/tests/test_discovery_and_ranking_bdd.py`
- `v2/search/tests/test_lang_biased_results.py`
- `v2/search/tests/test_show_search_service.py`
- `v2/search/tests/test_web_search_parity_bdd.py`

## Risks
- Changing `ShowSearchService` affects v3 and fuzzy/prefix paths.
- Locale → language-pool mapping is a frequent regression surface.
- Ranking/eval changes belong here — pair with `eval-writer.skill.md`.

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "lang_biased_results" --graph $GRAPH
graphify path "ShowSearchServiceV3" "ShowSearchService" --graph $GRAPH
```
