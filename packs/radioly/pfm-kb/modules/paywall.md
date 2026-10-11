# Paywall

Aliases: paywall, buy sheet, unlock sheet, coin sheet, subscription wall

## What It Is

The sheet the listener sees when they hit a lock: what they can buy or
watch-an-ad for. The **server** chooses the sheet and the plans from which
screen they came from.

## Actors

Listener on show page or player. After a successful pay, a different
“what you unlocked” sheet.

## Journey

1. Client says which screen (show, player, after pay) — not which journey
   type.
2. Server decides sheet kind, items, and plans.
3. After payment, threshold/pricing is skipped; the sheet is unlock
   confirmation.

## User-Visible Invariants

- The app must not send “I am on journey X.” That is server-owned.
- Player-from-ad and show-page locks can be different sheets.
- Do not invent plan prices or experiment splits here.

## Client Behavior

Needs network. Closing the sheet without paying leaves the episode locked.
