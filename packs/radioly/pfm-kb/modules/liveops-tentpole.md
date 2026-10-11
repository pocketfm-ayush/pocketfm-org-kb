# LiveOps tentpole

Aliases: liveops, tentpole, campaign billboard, episode zero

## What It Is
Timed branded campaigns injected into home, launch, Discover, autoplay, ads,
and My Store. Genre tentpoles can rotate featured shows weekly; direct campaigns
use fixed assets. Episode Zero can prepend promo assets on show details for
eligible low-playtime listeners.

## Actors
Pre-enrolled listener (device/genre). Campaign ops. Non-enrolled listeners see
nothing from tentpole (legacy festive may still apply separately).

## Journey
1. Open app / home — server checks locale, enrollment, active genre experiment.
2. Eligible variant → resolve week’s show + touchpoint assets.
3. Surfaces appear (billboard, module, banner, splash, bottom sheet, shorts, …).
4. Impressions count toward caps; capped touchpoints hide or re-rank.

## User-Visible Invariants
- No dedicated LiveOps screen — assets arrive inside normal feed/launch payloads.
- Caps stop repeat spam for a day/week window.
- Related: [home-feed](home-feed.md), [launch-config](launch-config.md),
  [discover-tab](discover-tab.md), [gtm-impressions](gtm-impressions.md).

## Gaps
- Live experiment IDs and enrollment lists are ops state — not packed here.
