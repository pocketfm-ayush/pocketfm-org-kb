# Kafka stream clients (workers)

Async Kafka consumers that finish listening progress, unlocks, wallet credits,
ads streaks, attribution, experience, feeds, and account side effects after
live APIs return.

**Modules**

- [kafka-workers](modules/kafka-workers.md)
- [listening-playtime](modules/listening-playtime.md)
- [video-impressions](modules/video-impressions.md)
- [show-unlocks-and-battle-pass](modules/show-unlocks-and-battle-pass.md)
- [wallet-coins-and-recon](modules/wallet-coins-and-recon.md)
- [subscription-lifecycle](modules/subscription-lifecycle.md)
- [ads-playtime-streaks-and-offerwall](modules/ads-playtime-streaks-and-offerwall.md)
- [s2s-attribution-and-moengage](modules/s2s-attribution-and-moengage.md)
- [experience-reengage-and-discover](modules/experience-reengage-and-discover.md)
- [feeds-packaged-deployment](modules/feeds-packaged-deployment.md)
- [account-actions-and-deactivation](modules/account-actions-and-deactivation.md)
- [comms-whatsapp-email-push](modules/comms-whatsapp-email-push.md)
- [referral-rewards](modules/referral-rewards.md)
- [budget-booster](modules/budget-booster.md)
- [content-throttling-rewards](modules/content-throttling-rewards.md)
- [continue-playing-cleanup](modules/continue-playing-cleanup.md)
- [reactivation-dumps](modules/reactivation-dumps.md)
- [autoplay-dumps](modules/autoplay-dumps.md)
- [auto-debit-reset](modules/auto-debit-reset.md)
- [be-events](modules/be-events.md)
- [character-sheets](modules/character-sheets.md)
- [content-moderation-ranking](modules/content-moderation-ranking.md)
- [machine-translation](modules/machine-translation.md)
- [mini-series-launch](modules/mini-series-launch.md)
- [user-default-tab](modules/user-default-tab.md)
- [loyalty-moengage-tags](modules/loyalty-moengage-tags.md)
- [entity-stats](modules/entity-stats.md)
- [feedback-popup](modules/feedback-popup.md)
- [appsflyer-device-campaign](modules/appsflyer-device-campaign.md)

**Flows**

- [purchase-to-entitlement-and-attribution](flows/purchase-to-entitlement-and-attribution.md)
- [listening-progress-persist](flows/listening-progress-persist.md)
- [ads-streak-and-offerwall-credit](flows/ads-streak-and-offerwall-credit.md)
- [experience-reengage-loop](flows/experience-reengage-loop.md)
- [account-deactivation-async](flows/account-deactivation-async.md)

Related: `radioly` (request path), `fabric` (platform playtime/impression),
`go-radioly-service` (Relay exporters), `airflow` (scheduled/Temporal jobs).
