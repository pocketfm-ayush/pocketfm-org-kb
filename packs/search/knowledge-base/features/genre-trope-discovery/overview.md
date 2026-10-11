# Genre / Trope Discovery

Aliases: empty search, empty query, genre discovery, trope

Product context: `search/pfm-kb/modules/genre-trope-discovery.md`

## What it is
Empty-query (and genre/topic) Search experience: fetch genres/modules from Radioly API,
attach tropes, surface curated discovery instead of text ES results.

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `GenreTropeService` | `v3/search/services/genre_trope_service.py` L60 | 59 | 17 |
| `GenreService` | `v3/search/services/genre_service.py` L12 | 39 | 10 |
| `TropeService` | `v3/search/services/trope_service.py` | — | — |
| Data maps | `v3/search/data/genre_trope_*.py` | 28 | — |

## Key edges
- `GenreTropeService` → `GenreService`, `TropeService` [INFERRED]
- Used by `UniversalSearchV3Handler`, `QueryRouter`, `UniversalSearchV3View` [INFERRED]
- `SearchRequestData.is_empty_query()` / `has_genre_or_topic()` gate this path (Community 36)

## Tests
- `v3/search/tests/test_v3_genre_discovery_bdd.py`
- `v3/search/tests/test_v3_genre_trope_data_bdd.py`
- Empty-query scenarios in `test_v3_universal_search_bdd.py`

## Risks
- Hardcoded genre/trope → show ID maps drift from CMS/product.
- Radioly API failure modes (empty genres, unreachable) covered in Community 30 tests.
- Platform-specific genre artwork lives on the universal-search BDD suite.

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "GenreTropeService" --graph $GRAPH
graphify query "how does empty query genre discovery work?" --graph $GRAPH --budget 4000
```
