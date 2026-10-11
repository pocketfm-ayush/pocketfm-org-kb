# Search features (from graph)

Product meaning: `search/pfm-kb/`. This folder is the code-grounded twin
(symbols, tests, graph). Each `overview.md` has `Aliases:` and
`Product context:`.

Feature knowledge derived from `search/graphify/graphify-out/` (code graph of
`pocket_search`). Each folder is one product/capability slice. Prefer these docs + the
graph over grepping when starting work.

**Graph snapshot:** see `GRAPH_REPORT.md` (rebuild when `pocket_search` HEAD moves).

| Feature | Key symbols | Primary code |
|---|---|---|
| [universal-search](universal-search/) | `UniversalSearchV3Handler`, `QueryRouter`, `universal_search()` | `v3/search/views.py`, `v2/search/views.py` |
| [language-biased-search](language-biased-search/) | `lang_biased_results()`, `ShowSearchService` | `v2/search/services/lang_biased_search.py`, `show_search.py` |
| [genre-trope-discovery](genre-trope-discovery/) | `GenreTropeService`, `GenreService`, `TropeService` | `v3/search/services/genre_*.py` |
| [show-filter](show-filter/) | `ShowFilterServiceV3` | `v3/search/services/show_filter_v3.py` |
| [me-show-exclusion](me-show-exclusion/) | `MEShowExclusionService` | `v2/search/services/me_show_exclusion_service.py` |
| [override-show-filter](override-show-filter/) | `OverrideShowFilterService` | `v2/search/services/override_show_filter_service.py` |
| [ai-pgc-replacement](ai-pgc-replacement/) | `apply_pgc_show_replacement()` | `v2/search/services/ai_pgc_show_service.py` |
| [campaign-only-shows](campaign-only-shows/) | `apply_campaign_only_show_filter()` | `v2/search/services/campaign_only_show_service.py` |
| [ds-thumbnails](ds-thumbnails/) | `ShowThumbnailService` | `v2/search/services/show_thumbnail.py` |
| [query-processing](query-processing/) | `removeLanguage()`, query normalize | `v2/search/query_processing.py` |
| [disabled-show-removal](disabled-show-removal/) | `UserDisabledShowRemovalService` | `v2/search/services/user_disabled_show_removal_service.py` |
| [response-caching](response-caching/) | `RedisUtils`, `get_universal_search_cache_key()` | `cache_key_utils.py`, `search_response_service.py` |

## How features compose (v3)

Typical v3 request path (from graph edges on `UniversalSearchV3Handler` / `QueryRouter`):

1. Parse → `SearchRequestData`
2. Route empty / genre / text query (`QueryRouter`)
3. Empty → genre-trope-discovery; text → language-biased-search / show-filter
4. Personalize: AI/PGC → campaign-only → ME exclusion → override filter → disabled shows → DS thumbnails
5. Cache via Redis (`RedisUtils`)

v3 still depends on v2 for `ShowSearchService`, `APIUserData`, and most personalization services.
