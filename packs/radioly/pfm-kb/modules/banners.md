# Promo banners

Aliases: player banner, show-page banner, feed banner, promo strip

## What It Is

The promo strip on player, show page, Home/feed, or web. The
**server** picks which one from the screen the app named.

Distinct from display / image ads (banner-ads).

## Actors

Listener on player, show page, or feed. Web (non-India) can see an
extra-coins store banner; web add-to-home can see a PWA banner.

## Journey

1. App says screen (player / show / feed / home) and, for player or
   show, the title and how many episodes are open.
2. Player: interactive or story-evolution, if present, **wins alone**.
   Else no-ad-pack, daily-unlock education, trial pack, or coin buy.
3. Some iOS listeners get trial / daily-unlock only on the internal
   image-ad path so the same strip is not shown twice.
4. Never-buyer, not brand-new: trial-pack strip is impression-capped
   per plan. A new plan resets the count.
5. Show page: first matching strip wins.

## User-Visible Invariants

- The app must not choose the journey type — only the screen.
- Empty list is success (no strip), not an error.
- Android uses a singular result; other platforms a list — same
  product.

## Client Behavior

Needs network. Closing a strip does not unlock anything.

## Gaps

Home lucky-spin contents, exact player waterfall after the exclusive
winners, and live trial prices are not recorded here.
