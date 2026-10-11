# Search — data / stores (index)

Owner repo: `pocket_search`.

## Sources

| Source | Use for |
|---|---|
| CODE SEARCH / MySQL mirrors | Show/thumbnail/locale filters |
| Elasticsearch aliases | Show docs / query sets / users |
| Argus warehouse | searchV3 clickstream / Android funnel |

## Pocket Search MySQL (`Meta.db_table`)

| Table | ORM | Path |
|---|---|---|
| `shows` | `Shows` | `v2/search/models.py` |
| `shows_thumbnail_mapping` | `ShowThumbnailMapping` | `v2/search/models_new/show_thumbnail.py` |
| `ai_pgc_show_mapping` | `AiPgcShowMapping` | `v2/search/models.py` |
| `show_locale` | `ShowLocale` | `v2/search/models.py` |
| `users` | `Users` | `v2/search/models.py` |
| `devices` | `Devices` | `v2/search/models.py` |
| `profiles` | `Profile` | `v2/search/models.py` |
| `countries` | `Country` | `v2/search/models.py` |
| `authorization` | `Authorization` | `v2/search/models.py` |
| `authentication` | `Authentication` | `v2/search/models.py` |
| `experiments` | `Experiment` | `v2/experiments/models.py` |
| `experiment_variants` | `ExperimentVariant` | `v2/experiments/models.py` |
| `kill_switch` | `KillSwitch` | `v2/common/kill_switch/models/kill_switch.py` |

## Elasticsearch aliases (code-referenced)

| Alias | Notes |
|---|---|
| `platform_show_alias` | Show documents (`ElasticService`) |
| `query_set_index_alias` | Query-set index |
| `user_index_alias` | User index |
| `comment_hashtag_alias` | Comment hashtags |

## Argus (search analytics)

| Table | Notes |
|---|---|
| `argus.prod.events_view_argus` | search / search_v2 / searchV3 |
| `spice_catalog.prod.clicks_per_day_funnel_android` | Android funnel agg |
| `bronze_catalog.clickstream.events` | Raw stream |

Radioly warehouse list: `radioly/knowledge-base/data/argus-warehouse.md`.
Radioly MySQL/Scylla: `mysql-orm-catalog.md`, `scylla-catalog.md`.

## Gaps

- No live ES `/_cat/indices` dump — only aliases referenced in code.
- App MySQL beyond the 13 mirrors above lives in radioly, not pocket_search.
