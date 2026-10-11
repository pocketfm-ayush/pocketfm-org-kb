# Cashback and reward wallet

Aliases: cashback, reward wallet, redeem rewards

Product context: `radioly/pfm-kb/modules/cashback.md`

## What it is

Currency wallet, not coins. Displayed spendable can be less than the
ledger. Earn is for non-spenders.

## Graph anchors

| Symbol | Source |
|---|---|
| cashback | `v3/cashback_and_rewards/` |


## Key product notes

A **currency** wallet (not coins). Earn from campaigns; spend on a coin
pack (and sometimes a no-ads bundle). Shown next to coins; they are not
the same balance.

## Risks

- Showing the raw ledger as spendable.
- Promising cashback on every purchase.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "cashback" --graph $GRAPH
```
