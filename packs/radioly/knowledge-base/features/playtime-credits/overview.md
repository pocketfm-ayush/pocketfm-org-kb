# Playtime credits

Aliases: playtime credits, Unlock+, hours pass

Product context: `radioly/pfm-kb/modules/playtime-credits.md`

## What it is

Time-based unlock credit / hours pass — not the same as coin balance.

## Graph anchors

CODE SEARCH `playtime_credit` / unlock-plus under payments / unlocking.

## Stores

- Related playtime KV: `audio_playtime.*` in `data/scylla-catalog.md`.


## Key product notes

A **time** wallet (hours / minutes), not coins. Some hours-pass
plans grant listen-time that unlocks episodes. History is this
ledger.

Paywall is still the sheet. Coins are a different balance.

## Risks

- Mixing playtime credits with spendable coins.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "playtime credits" --graph $GRAPH
```
