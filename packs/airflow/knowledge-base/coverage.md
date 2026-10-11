# Airflow pack coverage (vs Pocket-Fm/airflow)

**As of:** 2026-09-07 · **Ticket:** FMF-4712

## Source reality
- ~320 DAG Python files under `dags/` (+ domain code dirs)
- Temporal domains: content, ads, payments, experience, genai, platforms
- Top domain dirs: ads, payments, feed, experience, genai, moengage, novels,
  account_deactivation, ppv_validation, pocket_tv, marketing_campaign, search,
  social_notifications, meta, offline_experiment_allocations, shows, unlocking, …

## Pack counts
| Layer | Count |
|---|---|
| Feature overviews | 52 |
| pfm-kb modules | 52 |
| pfm-kb flows | 8 |

## Mapped product families
Content/feed, ads/offerwall, payments/recon/passes/TV, experience/streaks/referral/BT/Discover,
PPV validation, account lifecycle/churn, MoEngage/S2S/AppsFlyer/Meta audiences,
social/UGC notifications, offline experiment allocations, show catalog ops,
GenAI/TTS, search/novels analytics, platforms (stories metadata, SendGrid, experiment TTL),
Temporal per-domain workers, S2S mismatch validation, unlock tokenizer ops.

## Intentional SKIP (ops/infra)
`redis_analysis`, `db_monitor_jobs`, `db_dumps`, apollo/generic backfill tooling,
`profile_migration` one-off migrations, Scylla slow-query reports, API regression
harnesses, on-call redis key ops, `tmp`/`test_data`/`helper_scripts`.

## Honest gaps
- Not every individual DAG file has its own twin (by design — family twins).
- Live cron / allocation % / coin amounts not packed.
- Always verify DAG vs Temporal runtime before edits.
