# Radioly-related Argus warehouse tables

Source: Argus Knowledge Collection **`fm_product_analytics`** (queried 2026-09-02).
These are **Databricks** analytics tables, not live Radioly MySQL.

## Completeness

- Covers product analytics dimensions, playtime summaries, sessions, unlocks,
  shorts, events, monetization, subscriptions, experiments, ads, loyalty.
- Does **not** cover app MySQL (e.g. `shows_thumbnail_mapping`), Scylla
  playtime KV, or Elasticsearch indices.
- Prefer `argus.prod.*` over bronze passthroughs unless lineage is required.

## `argus.prod.*` — engagement / content

| Table | Notes |
|---|---|
| `fact_dau` | Daily active users |
| `user_show_summary` | Device × show playtime / listen depth |
| `user_story_summary` | Device/UID × story playtime |
| `fact_sessions` | Session-grain playtime |
| `shows` | Show dimension |
| `topics` | Topic / genre dimension |
| `fact_shows_stories_info` | Stories/episodes + show metadata |
| `fact_primary_show` | Primary show SCD |
| `show_trope_mapping` | Show ↔ trope |
| `tropes` | Trope dimension |
| `shorts` | Shorts dimension |
| `shorts_related_events_rm` | Shorts funnel events |
| `discover_tab_streams` | Shorts playtime streams |

## `argus.prod.*` — unlocks / buffer

| Table | Notes |
|---|---|
| `fact_user_show_unlock` | Unlock history |
| `fact_priority_zone_base` | Priority-zone episode bounds |
| `user_show_daily_buffer_based_du` | Daily unlock buffer |

## `argus.prod.*` — device / user dims

| Table | Notes |
|---|---|
| `fact_devices` | Device dimension |
| `fact_devices_with_reinstall_info` | Reinstall-aware devices |
| `device_level_user_mapping` | Device ↔ user |
| `user_level_device_mapping` | User ↔ device |
| `fact_user_info` | UID dimension |
| `revenue_tags_device_id_level_info` | Revenue tags (device) |
| `Playtime_Tags_Device_Id_Level_Info` | Playtime tags (device) |
| `RV_Tags_Device_Id_Level_Info` | RV tags (device) |
| `Revenue_Tags_UID_Level_Info` | Revenue tags (UID) |
| `Playtime_Tags_UID_Level_Info` | Playtime tags (UID) |
| `RV_Tags_UID_Level_Info` | RV tags (UID) |

## `argus.prod.*` — monetization / subs / experiments

| Table | Notes |
|---|---|
| `fact_overall_transactions_and_credits` | Txns + credits |
| `revenue_share_story_uid_pfm` | Revenue share |
| `coin_credit_source` | Coin credit source |
| `fact_subscription_plans_details` | Plan details |
| `fact_subscriptions` | Subscriptions |
| `fact_subscription_event_log` | Sub events |
| `fact_experiment_assignments` | Device experiment assign |
| `fact_experiment_assignments_uid` | UID experiment assign |
| `payments_streak` | Streaks |
| `fact_loyalty_events_log` | Loyalty |
| `ads_events_gold` | Ads events |
| `events_view_argus` | Clickstream (incl. searchV3) |

Low confidence (may be typo/alias): `fact_user_subs_event_log`.

## Bronze / spice (lineage — prefer gold)

| Table | Notes |
|---|---|
| `bronze_catalog.rds_fm.stories` | Prefer `fact_shows_stories_info` |
| `bronze_catalog.rds_fm.user_show_unlocks_tml` | Source of unlocks fact |
| `bronze_catalog.rds_fm.coin_plans` | No-ad-pack joins |
| `bronze_catalog.rds_fm.users` | Mentioned in onboarding funnel SQL (not fully documented) |
| `bronze_catalog.clickstream.events` | Raw clickstream |
| `spice_catalog.prod.clicks_per_day_funnel_android` | Android search funnel agg |

## Exhaustive Argus list (re-queried)

`ads_events_gold`, `coin_credit_source`, `device_level_user_mapping`,
`discover_tab_streams`, `events_view_argus`, `fact_dau`, `fact_devices`,
`fact_devices_with_reinstall_info`, `fact_experiment_assignments`,
`fact_experiment_assignments_uid`, `fact_loyalty_events_log`,
`fact_overall_transactions_and_credits`, `fact_priority_zone_base`,
`fact_primary_show`, `fact_sessions`, `fact_shows_stories_info`,
`fact_subscription_event_log`, `fact_subscription_plans_details`,
`fact_subscriptions`, `fact_user_info`, `fact_user_show_unlock`,
`fact_user_subs_event_log` (low confidence alias), `payments_streak`,
`Playtime_Tags_Device_Id_Level_Info`, `Playtime_Tags_UID_Level_Info`,
`revenue_share_story_uid_pfm`, `revenue_tags_device_id_level_info`,
`Revenue_Tags_UID_Level_Info`, `RV_Tags_Device_Id_Level_Info`,
`RV_Tags_UID_Level_Info`, `show_trope_mapping`, `shorts`,
`shorts_related_events_rm`, `shows`, `topics`, `tropes`,
`user_level_device_mapping`, `user_show_daily_buffer_based_du`,
`user_show_summary`, `user_story_summary`
(+ bronze/spice rows above).

Argus confirms: **no other catalogs** (no hive/redash/full `rds_fm` dump) are
documented in this KB. More warehouse tables may exist in Databricks metastore
but are outside `fm_product_analytics`.

## Not in Argus (use radioly ORM / Scylla)

- `shows_thumbnail_mapping` and other CMS/app MySQL tables → `mysql-orm-catalog.md`
- Scylla playtime/unlocks/ads/experience → `scylla-catalog.md`
- Live ES indices → search pack
