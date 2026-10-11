# Merchandise giveaway

Aliases: giveaway, merch giveaway, MVS giveaway, bottom slider gift

Product context: `radioly/pfm-kb/modules/giveaway.md`

## What it is

Merch entry for listeners already on a campaign. Not coins or cashback.
One entry per campaign.

## Graph anchors

| Symbol | Source |
|---|---|
| giveaway | `v3/giveaway/` |


## Key product notes

A merch entry form for listeners **already on a campaign** — not coins,
not cashback, not a store.

## Risks

- Entering someone who was never assigned.
- Treating slider absence as a wallet miss.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "giveaway" --graph $GRAPH
```
