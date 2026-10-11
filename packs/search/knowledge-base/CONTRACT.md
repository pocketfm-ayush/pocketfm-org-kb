# Repo Mind — pocket_search

Skills + orchestrator must obey this file and `contract.json`. Feature detail lives
in `features/`; the code graph lives in `../graphify/graphify-out/`.

**GitHub:** https://github.com/Pocket-Fm/pocket_search
**Stack:** Python · Django · Elasticsearch/OpenSearch · Redis · Scylla · MySQL

## Purpose

Pocket FM Search service: query normalization, language-biased show retrieval, genre/trope
discovery, personalization (AI/PGC, campaign, ME exclusion, overrides, disabled shows),
caching, and response formatting for mobile/web clients.

## Architecture map

| Layer | Location | Owns |
|---|---|---|
| HTTP (v2) | `v2/search/views.py`, `urls.py` | Thin adapters: `universal.search`, `show.search`, `user.search`, `query.auto_suggest`, … |
| HTTP (v3) | `v3/search/views.py`, `urls.py` | `UniversalSearchV3View` → `UniversalSearchV3Handler` + `QueryRouter` |
| Request | `v3/search/data/request_data.py`, `utils/request_parser.py` | `SearchRequestData` |
| Business logic | `v2/search/services/`, `v3/search/services/` | One service per concern |
| ES / ranking | `es_search_functions.py`, `lang_biased_search.py`, `show_search.py`, `sort_filter_utils.py` | Query DSL + ranking |
| Data access | `v2/search/repositories/` | Scylla / Redis / pair maps |
| Cache | `cache_key_utils.py`, `search_response_service.py`, `RedisUtils` | Keys, hit/miss, compress |
| Query cleanup | `query_processing.py` | Normalize query / strip language tags |
| Experiments | `v2/experiments/` | Feature gates |
| Tests | `v2/search/tests/`, `v3/search/tests/` | pytest + pytest-bdd |

**v2/v3 coupling (hard rule):** v3 is not standalone. `ShowSearchServiceV3` uses
`ShowSearchService`; v3 views use `APIUserData` and v2 personalization services. Changing v2
requires a v3 blast-radius check (`graphify explain` / `path`).

**Composition order (v3 personalize):** AI/PGC → campaign-only → ME exclusion → override →
disabled shows → DS thumbnails. Cache stores unpersonalized payloads (no uid/device in key).

## Conventions

- Validation / request parsing in views + `request_parser` / `SearchRequestData` — not buried in ES helpers.
- ES DSL stays in `es_search_functions.py` / `ShowSearchService` / `lang_biased_search.py`.
- Business rules in `services/`; repositories own external IO.
- Helpers must not make DB/Redis/ES calls.
- Functions stay short (PR checklist: avoid 20+ line monsters).
- No secrets in code; env/secrets_manager only.
- Prefer backward-compatible response shapes; if shape changes, **change the cache key**.
- New v3 import-chain modules must be added to BDD infra stubs.
- Prefer BDD (`pytest_bdd`) for user-visible behavior; plain pytest for unit internals.
- Before inventing structure: query the graph (`graphify query/explain/path`) and read
  `knowledge-base/features/<feature>/overview.md`.

## Allowed vs protected paths

See `contract.json` → `allowed_edit_paths` / `protected_paths`.

Patcher may write under `v2/search/**`, `v3/search/**`, `v2/experiments/**` only.
Never write mind, skills, agent, graphify, knowledge-base, or env/secret files.

## Definition of done

- [ ] Product questions from prd-analysis answered (or explicitly deferred in limitations)
- [ ] Evals from eval-writer encoded as failing-then-passing tests where applicable
- [ ] `make test` (or scoped `make test-v2` / `make test-v3`) passes
- [ ] `make lint` passes
- [ ] No weakening of assertions to make tests green
- [ ] Cache key reviewed if response shape changed
- [ ] v2/v3 blast radius considered
- [ ] Managed **Current API** block refreshed via mind-update (or confirmed unchanged)
- [ ] State ready for PR (`READY_FOR_PR`)

## External systems & mocking

Redis, Elasticsearch/OpenSearch, Scylla, MySQL, Radioly genre API, AppsFlyer.
Unit tests stub infra — never open real connections. Pattern:
`v3/search/tests/test_v3_universal_search_bdd.py` → `_stub_infra_modules()`.

## Commands

```bash
make test          # v2 + v3
make test-v2
make test-v3
make lint
make test-coverage # fails under ~78%
```

## Graph + knowledge

```bash
GRAPH=search/graphify/graphify-out/graph.json
graphify query "<question>" --graph $GRAPH
graphify explain "<symbol>" --graph $GRAPH
graphify path "<A>" "<B>" --graph $GRAPH
```

Feature packs: `search/knowledge-base/features/`.
Product meaning: `search/pfm-kb/`.
Tables / ES aliases: `search/knowledge-base/data/tables.md`.
Slug map: `search/knowledge-base/slug-map.yaml`.

<!-- BEGIN MANAGED: CURRENT_API -->
## Current API / behavior

### Endpoints

| Version | Path | Handler |
|---|---|---|
| v3 | `universal.search` | `UniversalSearchV3View` → `UniversalSearchV3Handler` |
| v2 | `universal.search` | `universal_search()` |
| v2 | `show.search` | `search_show()` |
| v2 | `user.search` | `search_user()` |
| v2 | `query.auto_suggest` | `query_auto_suggest()` |
| v2 | `hashtag.search` | `search_hashtag()` |
| v2 | `internal/universal_cache` | `cache_delete_prefix()` |
| v2 | `internal/update_show_details` | `s2s_update_show_details()` |

### v3 `universal.search` routing (`QueryRouter`)

- Empty query → genre/trope discovery (`GenreTropeService`)
- Genre/topic present → search/filter flow (`ShowFilterServiceV3` / show search)
- Otherwise → text search (`ShowSearchServiceV3` → `lang_biased_results` / `ShowSearchService`)

### v3 orchestration (`UniversalSearchV3Handler.build_response`)

1. Initialize shared services (Redis, disabled, ME, override, …)
2. Build cache key → read cache
3. **Cache hit:** personalize (AI/PGC, campaign, ME, override, …) → DS thumbnails → return
4. **Cache miss:** process search → apply filters → **cache unpersonalized** → personalize → DS thumbnails → return

Cache key must not include uid/device_id. Personalization always runs after cache read/write.

### Core services (today)

- Language-biased retrieval: `lang_biased_results()`, `ShowSearchService`
- Genre discovery: `GenreTropeService`, `GenreService`, `TropeService`
- Show filter (v3): `ShowFilterServiceV3`
- Personalization: `apply_pgc_show_replacement()`, `apply_campaign_only_show_filter()`,
  `MEShowExclusionService`, `OverrideShowFilterService`, `UserDisabledShowRemovalService`
- Thumbnails: `ShowThumbnailService` (DS + new-design mapping)
- Query cleanup: `removeLanguage()`, `query_processing.py`
- Cache: `get_universal_search_cache_key()` / v3 key helpers, `RedisUtils`, `redis_except()`

### Known intentional divergences

- Cache-hit vs fresh path: new-design thumbnail eligibility differs (hit: full design-revamp
  eligibility; fresh: web-only) — preserved intentionally in handler comments.
<!-- END MANAGED: CURRENT_API -->
