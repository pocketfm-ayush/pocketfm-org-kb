# My Store

Aliases: coin store, mini store, plans store

Product context: `radioly/pfm-kb/modules/my-store.md`

## What it is
Coin plans / store surfaces including injected promos (Budget Booster, LiveOps mystore banner).

## Graph anchors
| My store package | `v2/my_store/` |
| Plans services | `v2/payments/plans/` |
| BBD | `v3/budget_booster/` |


## Key product notes

The shop the listener opens to buy coins (and sometimes a pass).
Not the lock sheet. Not the coin balance.

The **server** picks the sections and the promos for this listener.

## Risks
- Packing live plan prices.
- Missing injected promo edges (BBD / LiveOps).

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "My Store" --graph $GRAPH
```
