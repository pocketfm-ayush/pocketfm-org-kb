# Show Filter (v3)

Aliases: genre filter, curated search, filter search

Product context: `search/pfm-kb/modules/show-filter.md`

## What it is
v3 path for genre-filter / curated-show search and response formatting when the request
carries filter context (not pure free-text ES). Uses `SearchRequestData` and title cleanup
via query-processing.

## Graph anchors
| Symbol | Source | Community | Degree |
|---|---|---|---|
| `ShowFilterServiceV3` | `v3/search/services/show_filter_v3.py` L18 | 36 | 18 |
| `SearchRequestData` | `v3/search/data/request_data.py` L9 | 36 | — |
| `build_search_request_data()` | `v3/search/utils/request_parser.py` L34 | 36 | — |

## Key edges
- Called from `._handle_search_query_flow()` in `v3/search/views.py` [EXTRACTED]
- Used by Handler / View / QueryRouter [INFERRED]
- Imports `removeLanguage()` for title stripping [EXTRACTED]

## Tests
- `v3/search/tests/test_v3_show_filter_bdd.py`
- Formatting helpers exercised from `test_user_experience_bdd.py` (`_format_show_via_v3`)

## Risks
- Shares Community 36 with request parsing — request-shape bugs look like filter bugs.
- Locale-aware filter behavior has dedicated BDD cases (`call_filter_with_locale`).

## Query
```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify explain "ShowFilterServiceV3" --graph $GRAPH
```
