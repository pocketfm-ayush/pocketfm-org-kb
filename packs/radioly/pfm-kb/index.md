# Radioly (FM consumer)

Feeds, library, show page, unlock, paywall, ads, wallet, Discover,
onboarding, and experience surfaces. Search is a separate product;
pair and campaign rules are shared in meaning, not in one service.

Screenshot ↔ API (Experience): `knowledge-base/architecture/api-to-screen.md`
(Confluence Content API Mapping). POD / onboarding: `architecture/content-pod.md`.

**Modules**

Home and catalog

- [home-feed](modules/home-feed.md)
- [default-feed-freshness](modules/default-feed-freshness.md)
- [visibility-filters](modules/visibility-filters.md)
- [ai-pgc-show-selection](modules/ai-pgc-show-selection.md)
- [bigger-thumbnails](modules/bigger-thumbnails.md)
- [device-cover-art](modules/device-cover-art.md)
- [player-feed](modules/player-feed.md)
- [autoplay-playlist](modules/autoplay-playlist.md)
- [cross-show-stitch](modules/cross-show-stitch.md)
- [community-updates](modules/community-updates.md)
- [comments-and-reviews](modules/comments-and-reviews.md)
- [key-tropes](modules/key-tropes.md)
- [ppv](modules/ppv.md)
- [not-interested](modules/not-interested.md)
- [topic-browse](modules/topic-browse.md)

Show, player, progress

- [show-details-and-unlock](modules/show-details-and-unlock.md)
- [listening-progress](modules/listening-progress.md)
- [downloads](modules/downloads.md)
- [player-chrome](modules/player-chrome.md)
- [episode-recap](modules/episode-recap.md)
- [show-ai-recap](modules/show-ai-recap.md)
- [character-chat](modules/character-chat.md)
- [character-cards](modules/character-cards.md)
- [interactive-story](modules/interactive-story.md)
- [story-evolution](modules/story-evolution.md)
- [car-mode](modules/car-mode.md)
- [alexa](modules/alexa.md)
- [sleep-mode](modules/sleep-mode.md)
- [tv-cast](modules/tv-cast.md)
- [writer-notes](modules/writer-notes.md)

Discover and first-run

- [discover-tab](modules/discover-tab.md)
- [stage](modules/stage.md)
- [pocket-pick](modules/pocket-pick.md)
- [onboarding-first-run](modules/onboarding-first-run.md)
- [onboarding-show-pick](modules/onboarding-show-pick.md)
- [trailer-code](modules/trailer-code.md)
- [campaign-deeplinks](modules/campaign-deeplinks.md)
- [library](modules/library.md)

Money and ads

- [paywall](modules/paywall.md)
- [my-store](modules/my-store.md)
- [checkout](modules/checkout.md)
- [subscriptions](modules/subscriptions.md)
- [coin-subscriptions](modules/coin-subscriptions.md)
- [coins-wallet](modules/coins-wallet.md)
- [playtime-credits](modules/playtime-credits.md)
- [author-gift](modules/author-gift.md)
- [pricing](modules/pricing.md)
- [auto-debit](modules/auto-debit.md)
- [payment-history](modules/payment-history.md)
- [cashback](modules/cashback.md)
- [giveaway](modules/giveaway.md)
- [new-user-coin-grant](modules/new-user-coin-grant.md)
- [gamified-rewards](modules/gamified-rewards.md)
- [rewarded-ads](modules/rewarded-ads.md)
- [banner-ads](modules/banner-ads.md)
- [in-player-ads](modules/in-player-ads.md)
- [no-ad-pack](modules/no-ad-pack.md)
- [banners](modules/banners.md)
- [offerwall](modules/offerwall.md)
- [app-open-ads](modules/app-open-ads.md)
- [sponsored-ads](modules/sponsored-ads.md)
- [airtel-premium](modules/airtel-premium.md)
- [partner-install-coins](modules/partner-install-coins.md)

Rewards and account

- [loyalty](modules/loyalty.md)
- [daily-checkin](modules/daily-checkin.md)
- [slot-machine](modules/slot-machine.md)
- [streaks](modules/streaks.md)
- [rewards](modules/rewards.md)
- [show-referral](modules/show-referral.md)
- [otp-login](modules/otp-login.md)
- [email-password-reset](modules/email-password-reset.md)
- [device-login-limit](modules/device-login-limit.md)
- [account-recovery](modules/account-recovery.md)
- [account-delete](modules/account-delete.md)
- [account-deactivate](modules/account-deactivate.md)
- [account-transfer](modules/account-transfer.md)
- [multi-profile](modules/multi-profile.md)
- [listener-profile](modules/listener-profile.md)
- [writer-profile](modules/writer-profile.md)
- [user-survey](modules/user-survey.md)
- [notification-permission](modules/notification-permission.md)
- [help-faq](modules/help-faq.md)
- [support-ticket](modules/support-ticket.md)
- [support-csat](modules/support-csat.md)
- [app-rating-popup](modules/app-rating-popup.md)
- [terms](modules/terms.md)
- [launch-overlays](modules/launch-overlays.md)

Platform identity and bootstrap

- [launch-config](modules/launch-config.md)
- [nexus-user-profile](modules/nexus-user-profile.md)
- [iam-identity](modules/iam-identity.md)
- [experiments-allocation](modules/experiments-allocation.md)
- [notification-inbox](modules/notification-inbox.md)
- [budget-booster](modules/budget-booster.md)
- [gtm-impressions](modules/gtm-impressions.md)
- [unlocking-byline](modules/unlocking-byline.md)
- [liveops-tentpole](modules/liveops-tentpole.md)
- [ugc-backend-writer](modules/ugc-backend-writer.md)
- [purchase-comms](modules/purchase-comms.md)
- [show-thumbnail-mapping](modules/show-thumbnail-mapping.md)
- [user-show-history](modules/user-show-history.md)

**Flows**

- [shared-with-search](flows/shared-with-search.md) — AI/PGC, campaign, thumbnails across Radioly + Search
- [open-app-with-launch-config](flows/open-app-with-launch-config.md)
- [users-devices-via-nexus-iam](flows/users-devices-via-nexus-iam.md)
- [liveops-across-surfaces](flows/liveops-across-surfaces.md)

- [launch-app](flows/launch-app.md)
- [first-run](flows/first-run.md)
- [open-from-campaign](flows/open-from-campaign.md)
- [open-home](flows/open-home.md)
- [open-show](flows/open-show.md)
- [open-player](flows/open-player.md)
- [open-discover](flows/open-discover.md)
- [finish-show](flows/finish-show.md)
- [buy-coins](flows/buy-coins.md)
- [watch-to-unlock](flows/watch-to-unlock.md)
- [auto-unlock-while-listening](flows/auto-unlock-while-listening.md)
- [unwind-from-home](flows/unwind-from-home.md)
- [talk-to-character](flows/talk-to-character.md)
- [login](flows/login.md)
- [switch-profile](flows/switch-profile.md)
- [recover-account](flows/recover-account.md)
- [close-account](flows/close-account.md)
- [claim-airtel-premium](flows/claim-airtel-premium.md)
- [ai-pgc-across-surfaces](flows/ai-pgc-across-surfaces.md)

**Gaps (do not invent):** live experiment %/winners, rail order,
prices, coin amounts, spin odds, listener PPV *pass* vs catalog PPV
test, offerwall live tasks/rates, Home hide after not-interested,
dedicated Trending tab (retired leftover list), old spend-loyalty
campaign (payout off),
contest landing besides Stage rails, Explore tab vs topic “see all”,
sponsored-series mid-roll vs session sheet, paid-download coin charge,
show SEO summary (CS dashboard), retired battle pass shop, retired
BT dashboard and top-shows smart caching.

Pack coverage vs `radioly_client_api` folders: `knowledge-base/coverage.md`.
