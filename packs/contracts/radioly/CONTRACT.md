# Repo Mind — radioly_client_api

Skills + orchestrator must obey this file and `contract.json`. Feature detail lives
in `features/` when present; the code graph lives in `../graphify/graphify-out/`.

**GitHub:** https://github.com/Pocket-Fm/radioly_client_api
**Stack:** Python · Django 5.1 · MySQL · Redis · Scylla · Elasticsearch · Kafka

## Purpose

FM consumer backend (Radioly): feeds, content, users, payments, ads, experience APIs for mobile/web.

Product meaning for listener surfaces: `radioly/pfm-kb/` (start at `index.md`).
Code-grounded twins: `features/` (ads, wallet, Discover, onboarding included).
Load matching `pfm-kb/` module for product meaning; do not invent from CONTRACT alone.

## Architecture map

| Layer | Location | Owns |
|---|---|---|
| HTTP / Django | `v2/, v3/, content_api/, feed_api/, user_api/` | ViewSets and URLs |
| Shared | `radioly_api/` | DB connections, middleware, secrets |
| Tests | `tests/, v2/tests/` | pytest |
| AI↔PGC selection | `v2/content_api/services/duplicate_show_service/` | `DuplicateShowService.is_show_eligible` |
| Pair config | `ExclusionConfigService`, table `ai_pgc_show_mapping` | CMS pair map + `keep_ai_default` |
| Feed filters | `v2/feed_api/helpers.py` | topic / library / show-feed / pre-slice |

**AI↔PGC (Radioly, not Search):** one ID from each CMS pair on feed surfaces.
Order: master kill → override → playtime ≥180s → `user_tg=pgc_<id>` pin →
cold-start (`keep_ai_default` else PGC). Admin:
`POST /v3/content/internal/ai_pgc_pair_config`. Search uses
`apply_pgc_show_replacement` in pocket_search. `ShowReplicaHelper` is the
older device-age replica map — not this flow. Detail:
`features/ai-pgc-show-selection/overview.md`.
Product context: `radioly/pfm-kb/modules/ai-pgc-show-selection.md`.

Query the graph before inventing structure:

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "<question>" --graph $GRAPH
graphify explain "<symbol>" --graph $GRAPH
graphify path "<A>" "<B>" --graph $GRAPH
```

## Conventions

- Python 3.13. `make test` runs pytest; `make ruff` is the lint gate.
- Secrets via secrets_manager / env — never commit credentials.
- CODEOWNERS: default @Pocket-Fm/fm-backend-leads; payments under monet-leads; ads under ads-backend-lead.

## Testing (critical for Groot draft PRs)

- Prefer **co-located** `test_*.py` next to the module
  (example: `v3/content/latam_modules/test_views.py` beside `views.py`).
- Do **not** assume a parent `tests/` folder covers the module. CI
  `scripts/get_impacted_tests.py` walks up to the nearest `tests/` dir and can
  select `v3/content/tests` while skipping `latam_modules/test_views.py` —
  that left radioly PR #32947 at **6% diff-cover** after pytest “passed”.
- When changing production code, Groot must run the discovered co-located
  tests (or the nearest real suite) **before** opening a draft PR. Phantom
  enqueue alone is not validation.
- PR workflow enforces **≥80% diff-cover** on changed production `.py` files.
  New branches / POST handlers / validators must be executed by those tests.
- Unit tests: no live MySQL/Redis/Scylla/ES/Kafka; follow existing fixtures.
- Review blockers that must not ship: null defaults that crash readers
  (e.g. `entities=None` + `json.loads`), cache invalidation that skips
  `LOCALE_CONST_MAPPING` remaps, missing auth/validation parity with PUT/GET.

## Allowed vs protected paths

See `contract.json` → `allowed_edit_paths` / `protected_paths`.
Never write knowledge-base, graphify, env, or secret files.

## External systems & mocking

mysql, redis, scylla, elasticsearch, kafka, s3.
Unit tests must not open MySQL, Redis, Scylla, ES, or Kafka. Follow existing pytest fixtures.

## Commands

```bash
make test
make ruff
```

## Rebuild graph

```bash
graphify extract <local-clone> --code-only --out radioly/graphify
graphify cluster-only radioly/graphify --no-label
```

## Knowledge layout

| Path | Role |
|---|---|
| `features/*/overview.md` | Code twin (symbols, edges, stores) |
| `pfm-kb/modules/`, `pfm-kb/flows/` | Product meaning (no code paths) |
| `architecture/api-to-screen.md` | Experience UI screen ↔ API path (screenshot debug) |
| `architecture/content-pod.md` | Content POD / onboarding Confluence pointers |
| `data/tables.md` (+ mysql/scylla/argus) | Table inventory — code-referenced, not live dump |
| `graphify/graphify-out/graph.json` | Discovery only — regenerate locally; never treat as truth |

Screen ↔ API source (images only in Confluence — pack stores paths, not secrets):
https://pocketfm-jira.atlassian.net/wiki/spaces/EW/pages/930251078/Content+API+Mapping+to+screens

Slug map (feature folder ↔ product module): see `knowledge-base/slug-map.yaml`.

## Gaps (honest)

- Feature overviews marked thin still need Graph anchors + store edges (see `features/README.md`).
- `data/*` catalogs are code-referenced inventories, not live `SHOW TABLES` / metastore.
- Column-level docs for most MySQL/Scylla tables are not packed — use CODE SEARCH / Argus.
- Folder coverage vs source: `knowledge-base/coverage.md` + `architecture/source-folder-map.md`.
- Nexus/IAM migration completeness is live (FMF-4712) — see `pfm-kb/flows/users-devices-via-nexus-iam.md`; do not claim zero MySQL without metrics.
- Cross-product AI/PGC + campaign + thumbnails: see `pfm-kb/flows/shared-with-search.md`.
- Volatile: live experiment %, prices, coin amounts — never invent.
