# Device cover art

Aliases: device-specific cover, DS thumbnail, personalised thumbnail,
per-device art

## What It Is

A **stamp** that can replace catalog cover art for this device, after
rails are built and visibility filters have run. It is not a Home rail
(that is bigger-thumbnails) and not a hide rule.

## Actors

The device. Editorial / catalog still own the fallback art. The
listener does not pick this cover.

## Journey

1. A surface returns titles (Home, library, player, show page, episode
   list, reviews, Discover, playlist, profile).
2. If this device has a cover for that title, the stamp replaces the
   image. Otherwise catalog art stays.
3. Audiobooks keep per-chapter art. The stamp must not overwrite those.

## User-Visible Invariants

- Same title can look different on two phones. That is expected.
- This is **device-scoped**, not login-scoped. Logout on the same
  phone does not restore catalog art. A new phone does not inherit it.
- Home-only thinking is wrong. Show page, library, player, and
  Discover can show the same stamp.
- Missing stamp is catalog art — not a broken feed.
- Bigger-thumbnails is a larger Home rail. Both can run.

## Client Behavior

Server-side stamp. The app renders the image it is given. Do not
re-stamp from another listener’s cache after logout.

## Gaps

- Which titles are targeted, and when a stamp expires or swaps.
