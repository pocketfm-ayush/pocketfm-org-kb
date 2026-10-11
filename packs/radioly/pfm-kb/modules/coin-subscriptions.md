# Coin pack subscriptions

Aliases: coin subscription, auto-renewing coin pack, subscribe to a
coin pack

## What It Is

A **recurring coin pack**: coins land in the same coin wallet as a
one-time pack, then the pack renews. Not the premium pass. Not
auto-unlock while listening.

## Actors

Logged-in listener on Store or after a one-time pack tap. Billing
renews, cancels, and pauses. The app does not flip “subscribed.”

## Journey

1. Eligible listeners (India / US, newer apps, logged in) may see
   auto-renewing packs next to one-time packs. Section order is
   server-owned.
2. After a one-time pack tap, some listeners get “subscribe to a
   coin pack instead?” with a matching-price auto-renew pack
   pre-selected. That sheet is capped (about 1/day, 2 lifetime).
3. Pay is checkout. Coins credit like a one-time pack.
4. Active list can show coin-pack subs **and** a premium pass
   together. “See all” appears when the list is long.
5. Cancel from Profile → Settings → Manage subscription.

## User-Visible Invariants

- Unused coins stay after the cycle. They are the same coins.
- Cancelled-but-valid, grace, paused-but-valid, and pending still
  look active until the window ends.
- Weekly vs monthly label follows the plan’s period (about a week
  or less is weekly). Do not invent the period.
- Do not treat this as the premium pass. Do not invent prices,
  plan IDs, or experiment splits.

## Client Behavior

Needs network and a login. Guests do not get this shop. Closing
the “subscribe instead?” sheet leaves them on the one-time pack.

## Product Source Of Truth

Server. The app must not send “I am on coin-sub.”

## Gaps

Which surfaces and which pack list are live now are not recorded
here.
