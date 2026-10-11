# Rewards (re-engage and where coins land)

Aliases: free coins, re-engage reward, coin congratulations

## What It Is

Not a listener catalog. Two different things:

1. **Ops-granted re-engage coins** — an internal list of listeners
   gets free coins. The listener did not tap “claim.” They may later
   see a congratulations slider and a path to My Store.
2. **Where gamification coins land** — daily check-in and Lucky Spin
   credit the **coin wallet**. That is not cashback and not the
   Reward Club bonus on a pack.

A separate **reward-wallet** balance can exist for campaign credits
(often non-spender, market-gated). Amounts are campaign-owned.

## Actors

Ops (internal) for re-engage lists. Listener only sees the after-credit
slider. Server owns credit and duplicate rejection.

## Journey

1. Ops submits a list: each row is a listener, a campaign, and a
   reward value. One campaign per file; no duplicate listener in the
   file or already stored for that campaign.
2. Valid rows are queued. Invalid or duplicate rows fail the batch.
3. After credit, an eligible listener can see “we added coins” and
   open My Store.

## User-Visible Invariants

- The listener cannot pick the amount. Do not invent it.
- Re-engage is not daily check-in, not Lucky Spin, and not Reward
  Club Plus.
- Coin wallet ≠ cashback. Cashback is a money product — do not
  document it here.

## Client Behavior

Slider needs the credit to already exist. Closing it does not remove
the coins. Needs network to show a current balance.

## Security / PII / Compliance

Re-engage ingest is ops-only. Do not expose it as a listener action.

## Gaps

Cashback campaigns, live reward-wallet eligibility, and the exact
re-engage coin amount are not recorded here.
