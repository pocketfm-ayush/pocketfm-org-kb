# Budget Booster

Aliases: BBD, budget booster deal, flash coin pack, rush offer

## What It Is
Personalized limited-time coin packs with boosted bonus coins. Injected into
My Store, payment options, player, and launch promo surfaces — not a standalone
tab. Pack assignment is sticky for the current sale/cycle window.

## Actors
Eligible listener (and guests mapped carefully). Payments/growth ops. CRM.

## Journey
1. Listener opens a payment or launch surface that asks for Budget Booster state.
2. Server picks active sale shape (event/flash over cyclic) and a sticky pack.
3. Surface shows urgency copy; purchase marks the window used (typically one buy).
4. Next window may reassign subject to market gates.

## User-Visible Invariants
- Mid-window segment changes should not swap the sticky pack.
- After purchase in a window, the offer should hide for that window.

## Gaps
- Live prices, calendars, and creatives are volatile — not packed here.
