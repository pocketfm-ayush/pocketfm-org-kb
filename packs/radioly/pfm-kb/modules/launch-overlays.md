# Launch and player overlays

Aliases: launch overlay, home popup, top nudge, bottom slider,
profile tooltip, player-open popup, player-minimise popup

## What It Is

At launch (and on player open / minimise) the server may attach **one
overlay per surface**. Surfaces: home popup, Home top nudge, profile
tooltip, bottom slider, player-open popup, player-minimise popup.

This is **not** the impression-ack. Ack only records that the listener
saw one. Serving happens on launch / player config.

Distinct from first-run permission screens, the Unwind **Home banner**
(a feed module), and the paywall sheet.

## Actors

Listener opening the app or the player. Server owns eligibility,
frequency, and which campaign wins a surface.

## Journey

1. Launch asks for overlays. Player open / minimise can ask again on
   those two surfaces.
2. Each surface gets at most one winner — or nothing.
3. If something shows, the app acks. Caps and “already seen” follow
   that ack, not the serve.
4. Newer Android subscription full-screen can arrive as a **launch
   deeplink** instead of the home popup. Same product intent; different
   pipe.

## User-Visible Invariants

- Do not invent which campaign wins a surface. Priority and live
  eligibility change.
- Empty is success (no overlay), not an error.
- Impression-ack is not an overlay catalog. Do not build overlays
  from an ack.
- First-run ATT / language / name screens are first-run, not this
  picker.
- Unwind’s evening **Home banner** is a feed module, not this picker.
  Unwind can still win the top nudge, profile tooltip, or a
  “you were in Unwind” relaunch popup in the same evening window.
- Player-minimise survey is this picker on the minimise surface —
  not a launch popup.
- Auto-unlock onboarding is this picker on **player-open**, not
  launch.
- After a long inactive gap, home popup and bottom slider can be
  suppressed for a short return window. Other surfaces are not
  automatically suppressed.
- Coin vs pass listeners see different eligible sets. Do not assume
  the same overlay.

## Client Behavior

Needs network. Closing an overlay does not unlock, check in, or
start Unwind. Showing without ack can show the same overlay again.

## Event Meaning

The ack is the “they saw it” event for frequency. Eligible / served
without ack is not a view.

## Product Source Of Truth

Server. The app names the surface, not the campaign.

## Gaps

- Which campaign wins, and current priority / frequency, are live
  state — not here.
- App-open / launch interstitials are a different product
  (app-open-ads). Do not serve them from this picker.
