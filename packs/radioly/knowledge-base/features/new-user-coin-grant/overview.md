# New user coin grant

Aliases: new user coins, free coins, germany coins

Product context: `radioly/pfm-kb/modules/new-user-coin-grant.md`

## What it is

Locale / campaign gated coin grant for new listeners.

## Graph anchors

CODE SEARCH `new_user` coin grant under payments / campaigns.


## Key product notes

A **one-time** coin grant for a new account (Germany campaign).
Not follow-for-coins. Not daily check-in.

## Risks

- Claiming grant amount or market without config evidence.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "new user coin grant" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

