# Rewards (re-engage)

Aliases: free coins, re-engage reward, coin congratulations

Product context: `radioly/pfm-kb/modules/rewards.md`

## What it is

Ops-granted re-engage coins plus where check-in / spin coins land
(coin wallet). Not cashback. Not Reward Club Plus. Not a listener
“claim” catalog.

## Graph anchors

| Symbol | Source |
|---|---|
| internal rewards | `v3/experience/rewards/` |


## Key product notes

Not a listener catalog. Two different things:

1. **Ops-granted re-engage coins** — an internal list of listeners
   gets free coins. The listener did not tap “claim.” They may later
   see a congratulations slider and a path to My Store.
2. **Where gamification coins land** — daily check-in and Lucky Spin
   credit the **coin wallet**. That is not cashback and not the
   Reward Club bonus on a pack.

A separate **reward-wallet** balance can exist for campaign credits
(often non-spender, market-gated). Amounts are campaign-owned.

## Risks

- Exposing re-engage ingest as a listener action.
- Mixing this with cashback or daily check-in.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "rewards" --graph $GRAPH
```
