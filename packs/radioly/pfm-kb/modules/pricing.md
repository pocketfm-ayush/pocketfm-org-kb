# Episode coin pricing

Aliases: billing pricing, coins required, episode price

## What It Is

Internal “what does this episode cost in coins for this listener?”
Not a shop the listener opens. Must match the show page.

Paywall still owns the sheet. Subscriptions own the pass.

## Actors

Other server callers, on behalf of a specific listener. Identity is
that listener’s, not the internal caller’s.

## Journey

1. Caller sends the show and episode range for a listener.
2. Server prices each episode the same way show-open does, then
   applies the same coin discount (floor 1 coin).
3. Response is coins now and coins before discount (strike-through
   when they differ).

## User-Visible Invariants

- A price that disagrees with the show page is a product bug.
- Do not invent coins, plan IDs, or experiment splits.
- Only episode pricing exists here.

## Gaps

Battle-pass titles may not match the show page (source-noted). Treat
as open. Live discount % is not recorded here.
