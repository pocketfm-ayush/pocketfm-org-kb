# radioly_client_api → pack map

| Source | Owns (product) | Pack entry |
|---|---|---|
| `v2/feed_api`, `v3/feed*` | Home, launch config, charts, onboarding feeds | home-feed, launch-config |
| `v2/feed_api/billboards` | Web Billboard / Premiere language lists | web-billboard |
| `v2/content_api`, `v3/content*` | Show page, unlock, AI↔PGC, ads helpers | show-details-unlock, ai-pgc-show-selection |
| `v2/user_api`, `v3/user*` | Auth, profile, history, device | otp-login, listener-profile, user-show-history |
| `v2/payments`, `v3/payments`, `v2/wallet` | Plans, checkout, wallet, subs | paywall, checkout, coins-wallet, subscriptions |
| `v2/ads`, `v3/ads` | Rewarded / RV / streaks | rewarded-ads, … |
| `v3/experience` | Referral, bigger thumbnails, … | show-referral, bigger-thumbnails |
| `v2/campaigns`, `v3/gtm` | GTM / incent / impressions publish | gtm-impressions, launch-overlays |
| `v2/experiments` | Allocation helpers | experiments-allocation |
| `v3/liveops` | Tentpole / Episode Zero injects | liveops-tentpole |
| `external_services/nexus` | Non-PII user/device attributes | nexus-user-profile |
| `external_services/iam` | Identity / PII / device accounts | iam-identity |
| `external_services/ugc_backend` | Writer profile-state + delete sync | ugc-backend-writer |
| `v3/budget_booster` | Personalized coin-deal packs | budget-booster |
| `v3/unlocking_byline` | Unlock labels on show page | unlocking-byline |
| `radioly_api` | Shared DB/Redis/secrets | CONTRACT only |
| `v3/drs`, `fraud_detection`, `circuit_breaker` | Ops resilience / fraud | No product twin |
| `quality_gating` | Internal quality | No product twin |

Legacy top-level `content_api/`, `feed_api/`, `user_api/` still exist beside `v2/` —
prefer v2/v3 paths unless CODE SEARCH proves otherwise.
