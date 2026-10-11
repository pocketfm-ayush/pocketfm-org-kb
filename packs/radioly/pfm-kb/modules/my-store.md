# My Store

Aliases: store, coin store, my store, promotions, mini store

## What It Is

The shop the listener opens to buy coins (and sometimes a pass).
Not the lock sheet. Not the coin balance.

The **server** picks the sections and the promos for this listener.

## Actors

Listener on Store. Login preferred. Guests can still see a shop;
balances and buys need a login.

## Journey

1. App opens Store (or a thinner **mini store** from bulk unlock).
2. Server returns section order, promos, FAQ, and balances together
   or as separate reads. Same meaning.
3. Listener picks a pack, a pass, earn-coins, or a promo.
4. Pay is checkout. Coins land in the coin wallet.

## User-Visible Invariants

- Layout is server-owned. Do not hardcode section order.
- Mini store has no wallet strip. Full Store can show coins **and**
  reward cash. They are not the same balance.
- Some pass-only listeners see just the premium-pass block.
- One-time coin packs and auto-renewing coin packs can both appear.
  Auto-renewing coin packs are not the premium pass.
- Store copy: coins do not expire; they cannot move between accounts.
- Web can show extra coins on site buys. That offer is server-owned.
  Do not invent the percent. India web does not get that welcome bonus.
- Do not invent pack prices, plan IDs, or which promo is live.

## Client Behavior

Needs network. A blank Store is “nothing to show,” not “store is
down.” Closing Store without paying leaves the balance unchanged.

## Product Source Of Truth

Server. The app must not send “show layout X.”

## Gaps

Which promo, earn-coins block, or pack family is live now is not
recorded here.
