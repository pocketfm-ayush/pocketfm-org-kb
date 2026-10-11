# Airtel premium

Aliases: airtel, airtel premium, airtel claim

Product context: `radioly/pfm-kb/modules/airtel-premium.md` · flow `radioly/pfm-kb/flows/claim-airtel-premium.md`

## What it is

Carrier-partner premium claim path for eligible Airtel listeners.

## Graph anchors

CODE SEARCH `airtel` under payments / campaigns / subscriptions.


## Key product notes

A **carrier-granted** Pocket Premium window. Airtel starts an order;
the listener claims it on a Pocket FM web page. This is not a store
buy and not Reward Club.

The window is **90 days**. Lifetime: one successful claim per login.

## Risks

- Claiming entitlement rules without partner/config evidence.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "airtel premium" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

