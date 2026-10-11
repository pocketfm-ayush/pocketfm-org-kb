# Playtime credits (Unlock+)

Aliases: playtime credit, hours pass, Unlock+, listen-time wallet

## What It Is

A **time** wallet (hours / minutes), not coins. Some hours-pass
plans grant listen-time that unlocks episodes. History is this
ledger.

Paywall is still the sheet. Coins are a different balance.

## Actors

Logged-in listener on an hours-pass. Billing grants and expires
the time.

## Journey

1. Eligible hours-pass becomes active. Remaining time can show as
   PLUS / hours left.
2. Unlock spends minutes from this wallet, not coins.
3. History lists grants (pass credit) and spends (title + episode)
   as +/− hours or minutes.
4. When the pass expires or goes inactive, leftover time zeros.
   History shows that expiry.

## User-Visible Invariants

- This is not coins and not reward cash. Do not mix the ledgers.
- You cannot read another account’s time history.
- Only some hours-pass plans grant this. Do not assume every
  premium pass has minutes.
- Do not invent hours, plan IDs, or which markets are live.

## Client Behavior

Needs network and a matching login. History lives on the account.

## Gaps

Which hours-pass plans and markets are live now are not recorded
here.
