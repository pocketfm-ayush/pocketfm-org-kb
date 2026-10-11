# Buy coins

Participating modules: my-store, checkout, coins-wallet, cashback,
coin-subscriptions.

## Journey

1. App opens Store (or mini store). Server owns sections and packs.
2. Listener picks a **one-time** pack, or — if offered — an
   auto-renewing coin pack. Reward cash can pay a pack when shown.
3. Checkout: how to pay (site vs in-app, when shown), then market
   pay methods, then confirm.
4. Coins land in the coin wallet. Reward cash is unchanged unless
   that was the tender.
5. Success chrome can follow. History can show the buy.

## User-Visible Invariants

- Store does not credit. Confirm does.
- Auto-renewing coin pack ≠ premium pass.
- Reward cash ≠ coins. Displayed reward cash can be less than the
  ledger (hold).
- Do not invent pack prices, extra-coin percent, or plan IDs.

## Failure modes

- Already paid / duplicate confirm → visible fail; no second credit.
- Refund started → no coins.
- Not enough reward cash → fail, coins unchanged.
- How-to-pay or checkout closed → balance unchanged.
