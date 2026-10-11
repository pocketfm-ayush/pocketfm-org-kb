# Brand-sponsored session

Aliases: sponsored ad, brand unlock sheet, sponsored next episode

## What It Is

A **brand sheet** (“a brand is sponsoring your next episode”):
watch a short message, one episode opens. Not a display still
(banner-ads), not a mid-roll (in-player), not the lock-sheet
watch-to-unlock pack (rewarded-ads). No coins.

## Actors

Listener. The server decides if a session is on and which brand
copy. Decline is fine.

## Journey

1. App asks if a sponsored session is available.
2. Sheet: accept → short message → that next episode opens.
   Decline → sheet goes away. Nothing unlocks.
3. After a session, a quiet day: do not show another.

## User-Visible Invariants

- Brand title, art, and offer are server-owned. Do not invent a
  brand or a coin reward.
- Empty ask is success (no sheet), not an ad outage.
- This is not a Home/player still and not a mid-roll.

## Client Behavior

Needs network. Closing without accepting leaves the episode
locked.

## Event Meaning

Accept + finished message is the unlock. Fetching the sheet is
not.

## Gaps

- Which brand and market are live.
- A separate “sponsored series” mid-roll flag is unproven as
  this same product.
