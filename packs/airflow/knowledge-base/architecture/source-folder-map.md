# airflow repo → pack map

| Source | Product role | Pack entry |
|---|---|---|
| `dags/` | Classic Airflow schedules | airflow-dags + domain twins |
| `temporal/content` | Content Temporal worker | temporal-content-worker |
| `temporal/ads` | Ads Temporal worker | temporal-ads-worker |
| `temporal/payments` | Payments Temporal worker | temporal-payments-worker |
| `temporal/experience` | Experience Temporal worker | temporal-experience-worker |
| `temporal/genai` | GenAI Temporal worker | temporal-genai-worker |
| `temporal/platforms` | Platforms Temporal worker | temporal-platforms-worker |
| `feed/`, `shows/` | Feed/content job code | content-* twins |
| `ads/` | Ads job code | ads-* twins |
| `payments/`, `unlocking/`, `pocket_tv/` | Payments/TV | payments-* / pocket-tv-payments |
| `experience/`, `loyalty_tier_program/` | Experience/loyalty | experience-* twins |
| `genai/` | TTS / genre / comments | tts-audio-pipelines, auto-genre-tags |
| `moengage/`, `marketing_campaign/`, `s2s_*` | CRM / growth | moengage-crm-sync, s2s-attribution-jobs, appsflyer-audience-export |
| `ppv_validation/` | PPV live eligibility | ppv-validation-pipeline |
| `account_deactivation/`, `churn_reactivation/` | Account lifecycle | account-lifecycle, churn-reactivation-coins |
| `novels/`, `search/` | Novels/search jobs | novels-analytics-jobs, search-index-jobs |
| `redis_analysis/`, `db_*` | Ops | No product twin |

| `social_notifications/` | social-ugc-notifications |
| `offline_experiment_allocations/` | offline-experiment-allocations |
| `meta/` | meta-audience-sync |
| `marketing_campaign/` | appsflyer-audience-export, facebook-campaign-insights, meta-audience-sync |
| `shows/` | show-catalog-ops |
| `s2s_validation/` + `s2s_events/` | s2s-mismatch-validation, s2s-attribution-jobs |
| `unlocking/` | unlock-tokenizer-ops (+ user-show-unlock-sync) |
| `experiment/` | experiment-health-jobs |
| `profile_migration/` | intentional SKIP (one-off) |
