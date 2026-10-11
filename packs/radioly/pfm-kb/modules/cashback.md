# Cashback and reward wallet

Aliases: cashback, reward wallet, redeem rewards

## What It Is

A **currency** wallet (not coins). Earn from campaigns; spend on a coin
pack (and sometimes a no-ads bundle). Shown next to coins; they are not
the same balance.

## Actors

Logged-in listener. Earn is for non-spenders on supported markets.
Spend is anyone with reward balance.

## Journey

1. Wallet shows coins **and** reward cash, plus an expiry line when
   some of the cash will lapse.
2. Spend picks a coin pack and pays with reward balance.
3. Not enough reward cash fails. Success credits coins (and may add
   no-ads days).

## User-Visible Invariants

- Displayed reward cash can be less than the ledger (hold / lien).
  Do not show the raw ledger as spendable.
- Rewards can expire; the expiry line is product-visible.
- Earn is not for existing spenders. Do not promise cashback on
  every purchase.
- Unknown markets use US packs unless international pricing is on.
  India stays India. Do not invent pack prices.

## Client Behavior

Needs network and a login. Spend is rate-limited; a sudden “try again”
is expected, not a missing wallet.

## Gaps

Current campaign, earn amounts, and referral/loyalty meaning are live
state — not here.
