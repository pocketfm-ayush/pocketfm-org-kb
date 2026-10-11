# Open a show

Participating modules: show-details-and-unlock, ai-pgc-show-selection,
paywall.

## Journey

1. App opens show page or player.
2. Visible ID (hidden / pair / region).
3. If paired, keep the side with more unlock progress; copy AI → PGC
   progress when redirecting.
4. Compute open episode count (daily unlock at most once per day).
5. Locked tap → paywall. Server picks the sheet from the screen.
   After pay → unlock confirmation, not a new price.

## User-Visible Invariants

- Losing durable unlock state looks like lost episodes.
- Paywall journey type is not a client field.

## Failure modes

- Unlock service dark or timed out → legacy in-process unlock. Same
  product, do not tell the user “unlock is down.”
- Pair compare unavailable → do not invent progress; fail toward the
  requested show.
