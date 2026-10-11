# Query Processing

Aliases: query normalize, strip language, clean query, title cleanup

Product context: `search/pfm-kb/modules/query-processing.md`

## What it is
Normalize/clean search queries and show titles: strip unsafe characters, extract language
tags, remove parenthesised language suffixes from ES titles, spam/mash detection helpers.

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `removeLanguage()` | `v2/search/query_processing.py` L108 | 42 | 10 |
| Query processing module | `v2/search/query_processing.py` | 42 | — |
| Spam / mash heuristics | helpers near Community 41 | 41 | — |

## Key edges
- Used by v2 views, v3 views, `ShowFilterServiceV3`, `search_response_service`
  (`strip_language_from_english_titles`) [EXTRACTED]
- BDD: `test_query_normalization_bdd.py` Community 34

## Tests
- `v2/search/tests/test_query_normalization_bdd.py`

## Risks
- Title stripping affects displayed English titles and filter formatting — regressions are
  user-visible.
- Shared by v2 and v3; one bug hits both.

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "removeLanguage" --graph $GRAPH
```
