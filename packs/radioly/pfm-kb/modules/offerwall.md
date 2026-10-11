# Offerwall

Aliases: offer wall, earn coins tasks, incent offers

## What It Is

A **task wall** for coins: install, survey, follow, purchase, and
similar offers. Opens as an offer-wall screen. Not watch-an-ad
(that is rewarded-ads).

## Actors

Listener (usually logged-in). The server lists offers and credits.

## Journey

1. App opens the wall from store / rewards / a promo.
2. Server returns the current offer list (or hides the wall).
3. Listener finishes a task.
4. Credit lands after completion is confirmed — opening the wall
   does not pay.

## User-Visible Invariants

- Watching a Pocket FM ad is not this wall.
- Caps and “come back later” are expected.
- Completed tasks can appear in a **history** list. Fetching history
  is not credit.
- Watch-an-ad proof / acknowledge is rewarded-ads, not this wall.
- Do not invent which offers or coin amounts are live.

## Client Behavior

Needs network for the list and again for credit. Closing mid-task
leaves coins uncredited.

## Gaps

Live offers, exchange rates, and which sale is on are not recorded
here.
