# Radioly — data tables (index)

Owner repo: `radioly_client_api`.

## Three sources — do not conflate

| Source | What it is | When to use |
|---|---|---|
| **CODE SEARCH / MySQL ORM** | App MySQL (`Meta.db_table`) | Table named in Slack/code, columns, `props` |
| **CODE SEARCH / Scylla** | Operational KV (`keyspace.table`) | Playtime, unlocks, ads, experiments state |
| **Argus `fm_product_analytics`** | Databricks warehouse (`argus.prod.*`) | Analytics SQL, aggregates, funnels |

Argus does **not** document most app MySQL or Scylla tables. Example:
`shows_thumbnail_mapping` is **absent** from Argus — answer from ORM + feature overview.

## Pack files

| File | Contents |
|---|---|
| `data/mysql-orm-catalog.md` | **~271** Django `db_table` (+ raw SQL) names |
| `data/scylla-catalog.md` | **~81** `keyspace.table` refs from radioly code |
| `data/argus-warehouse.md` | Warehouse tables from Argus (verified) |
| `features/*/overview.md` | Per-feature schema notes |

## Honest gaps

- Catalogs are **code-referenced** inventories, not a live `SHOW TABLES` / metastore dump.
- Argus KB documents ~40 warehouse tables; bronze `rds_fm` may mirror more MySQL
  tables that are **not listed** in Argus docs (only `stories`, `coin_plans`,
  and a mention of `users` appear).
- Scylla tables that exist in the cluster but are never referenced in this
  checkout will not appear in `scylla-catalog.md`.

## Hot app tables

| Table / store | Feature / note |
|---|---|
| `shows`, `stories`, `topics` | Core content (MySQL) |
| `shows_thumbnail_mapping` | `features/show-thumbnail-mapping/` |
| `ai_pgc_show_mapping` | `features/ai-pgc-show-selection/` |
| `audio_playtime.device_story_playtime` / `user_story_playtime` | `features/user-show-history/` |
| `show_unlocks.user_show_unlocks` / `device_show_unlocks` | Unlock state (Scylla) |
| `users`, `devices`, `user_activity` | Identity / activity |
| `user_coin_wallet`, `transactions` | Wallet / payments |

## Answer recipe

1. Infer repo (`shows_thumbnail_mapping` / `show.*` → radioly).
2. CODE SEARCH ORM / Scylla / view.
3. Call Argus **only** if warehouse/SQL **or** table is in `argus-warehouse.md`.
4. Cite pack path + code path; never invent columns.

## Still open

- Column-level docs for most of the 271 MySQL / 81 Scylla tables are not packed.
- Prefer CODE SEARCH on the ORM path in `mysql-orm-catalog.md` / Scylla path in
  `scylla-catalog.md` before calling Argus.
- Live `SHOW TABLES` / Scylla describe / ES `/_cat/indices` dumps are out of scope
  until generated and reviewed.

