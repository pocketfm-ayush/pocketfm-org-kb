# Coin pack subscriptions

Aliases: coin subscription, auto-renewing coin pack

Product context: `radioly/pfm-kb/modules/coin-subscriptions.md`

## What it is

Recurring coin pack. Same coin wallet as a one-time pack. Not the
premium pass. Not auto-unlock.

## Graph anchors

| Symbol | Source |
|---|---|
| coin subscriptions | `v3/payments/coin_subscriptions/` |


## Key product notes

A **recurring coin pack**: coins land in the same coin wallet as a
one-time pack, then the pack renews. Not the premium pass. Not
auto-unlock while listening.

## Risks

- Calling this the premium pass.
- Flipping “subscribed” on the client.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "coin subscriptions" --graph $GRAPH
```
