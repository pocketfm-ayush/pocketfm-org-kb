# Radioly pack coverage (vs radioly_client_api)

**As of:** 2026-09-07 · **Ticket:** FMF-4712

## Source folder → KB status

| Source area | Pack coverage | Notes |
|---|---|---|
| `v2/feed_api`, `v3/feed*` | home-feed, default-feed-cache, player-feed, launch-config, liveops-tentpole, web-billboard | Launch + LiveOps inject; web Billboard lists are `web_constants.py` |
| `v2/content_api`, `v3/content*`, `v3/unlocking*` | show-details-unlock, unlocking-byline, AI-PGC, visibility | Byline is copy-only |
| `v2/payments`, `v3/payments`, `v2/wallet`, `v2/my_store` | paywall, checkout, coins, subscriptions, pricing, purchase-comms | Strong |
| `v2/ads`, `v3/ads` | rewarded, banner, in-player, offerwall, no-ad-pack | Strong |
| `v3/experience`, Discover, Stage | discover, stage, referral, bigger-thumbnails | Studio rename under stage |
| `v2/user_api`, account flows | otp, delete/deactivate, recovery, transfer, multi-profile | Strong |
| `external_services/nexus` | nexus-user-profile | FMF-4712 |
| `external_services/iam` | iam-identity | FMF-4712 |
| `external_services/ugc_backend` | ugc-backend-writer | Writer achievements + delete sync |
| `v2/experiments` | experiments-allocation | No live % packed |
| `v2/notification`, push | notification-inbox | |
| `v2/email`, `v2/whatsapp_notification` | purchase-comms | Locale-gated WhatsApp |
| `v3/budget_booster` | budget-booster | |
| `v3/impression`, `v3/gtm` | gtm-impressions | Fabric stores counts |
| `v3/liveops` | liveops-tentpole | Listener-visible injects |
| `v2/segmentation_engine` | Noted under Nexus/ads — no separate twin | Legacy bitmaps |
| `v2/rule_engine` | Noted under pricing (HarperCollins) — no twin | Admin/ops |
| `v3/drs`, `fraud_detection`, `circuit_breaker` | Ops/infra — no listener pfm-kb | Intentional |
| `v3/crosswalk_ds` | Folded into bigger-thumbnails notes | Not separate module |
| CS-DB / SEO / retired BT / battle-pass shop | **Do not twin** | features/README |

## Counts

| Layer | Count |
|---|---|
| Feature overviews | 100 |
| pfm-kb modules | 100 |
| pfm-kb flows | 23 |
| Catalog ↔ features ↔ modules | Aligned via slug-map |

## Honest remaining gaps

- Live experiment allocation %, prices, coin amounts, spin odds
- Offerwall live tasks/rates
- Listener PPV *pass* vs catalog PPV test nuance
- Full MySQL/Scylla column docs (use data/ + Argus/CODE SEARCH)
- File/function encyclopedia — use graphify, not pfm-kb
- Some feature overviews remain shorter than ideal; high-traffic ones thickened
