# kafka-stream-clients pack coverage

**As of:** 2026-09-07 · **Ticket:** FMF-4712

## Source reality
- ~38 `workers/` domain directories + many root-level worker modules
- Three K8s entry scripts: `workers-kafka-critical.sh`, `workers-kafka-consumer.sh`,
  `workers-kafka-db-s3.sh` (dozens of named replicas)
- Shared `utils/`, `bloom/`, `config.yaml`, novels kafka ini

## Pack counts
| Layer | Count |
|---|---|
| Feature overviews | 29 |
| pfm-kb modules | 29 |
| pfm-kb flows | 5 |

## Folder / pipeline map (product twin status)

| Source area | Status | Twin(s) |
|---|---|---|
| `workers/streaming` audio | covered | listening-playtime |
| `workers/streaming` video | covered | video-impressions |
| `workers/user_show_playtime*` | covered | listening-playtime |
| `workers/battle_pass_user_show_unlock`, device_show_status | covered | show-unlocks-and-battle-pass |
| `workers/payments`, partnership_campaign | covered | wallet-coins-and-recon |
| `workers/subscription_*` | covered | subscription-lifecycle |
| `workers/advertisement`, streak_retain*, reset_rv_keys, tapjoy/DT webhooks | covered | ads-playtime-streaks-and-offerwall |
| `workers/s2s_events_v2` | covered | s2s-attribution-and-moengage |
| `workers/experience` | covered | experience-reengage-and-discover |
| `workers/packaged_deployment`, feeds | covered | feeds-packaged-deployment |
| `workers/user_actions`, deactivation, delete OTP | covered | account-actions-and-deactivation |
| `workers/communication`, emails, moengage push | covered | comms-whatsapp-email-push |
| `workers/referral`, show_referral_reward | covered | referral-rewards |
| `workers/budget_booster_pack` | covered | budget-booster |
| `workers/content_throttling_v2` | covered | content-throttling-rewards |
| `workers/continue_playing_show_deletion` | covered | continue-playing-cleanup |
| `workers/reactivation` | covered | reactivation-dumps |
| `workers/autoplay` | covered | autoplay-dumps |
| auto debit reset workers | covered | auto-debit-reset |
| `workers/be_events` | covered | be-events |
| `workers/character_sheets` | covered | character-sheets |
| `workers/content`, spam_comments | covered | content-moderation-ranking |
| `workers/machine_translation` | covered | machine-translation |
| mini series launch | covered | mini-series-launch |
| user default tab | covered | user-default-tab |
| loyalty/spending moengage | covered | loyalty-moengage-tags |
| entity stats | covered | entity-stats |
| feedback popup | covered | feedback-popup |
| appsflyer device campaign | covered | appsflyer-device-campaign |
| `workers/mongo_stream`, `migrations`, `document_templates` | intentional SKIP | ops/legacy low product signal |
| `workers/novels_ds_pd`, `script_summarization` | intentional thin | verify before expanding |
| `utils/`, `bloom/`, `tests/` | intentional thin | shared infra/harness |

## Intentional SKIP
- One overview per replica line in workers-kafka-*.sh
- Live topic names encyclopedia (read constants/source)
- Secrets / partner API credentials

## Honest gaps
- Family twins ≠ every consumer class
- Always confirm **Relay vs kafka-stream-clients** for S2S events
- Always confirm **Fabric vs these workers** for playtime
- Always confirm **Airflow vs these workers** for recon/referral/account batches
