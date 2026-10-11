# Partner install coins

Aliases: partner install, install coins, affiliate coins

Product context: `radioly/pfm-kb/modules/partner-install-coins.md`

## What it is

Coin credit for partner / affiliate install campaigns.

## Graph anchors

| Symbol | Source |
|---|---|
| affiliate helpers | `v2/campaigns/affiliate_program/services/affiliate_program.py` |


## Key product notes

A **one-time coin grant** after a partner install or promo
redeem (device starts it; login collects it). Not Reward Club.
Not Germany new-user coins. Not offerwall. Not ops re-engage.

## Risks

- Treating affiliate credit as ordinary store purchase.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "partner install coins" --graph $GRAPH
```
