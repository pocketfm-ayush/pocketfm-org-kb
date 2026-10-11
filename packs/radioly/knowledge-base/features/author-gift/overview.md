# Author gift

Aliases: gift coins, send gift, gift to author

Product context: `radioly/pfm-kb/modules/author-gift.md`

## What it is

Spend own coins on an author. Not unlock. Not a wallet transfer.

## Graph anchors

| Symbol | Source |
|---|---|
| author gift | `v2/wallet/gift_viewsets.py` |


## Key product notes

The listener spends **their** coins on an author for a chapter.
Not unlock. Not a transfer to another listener wallet.

## Risks

- Treating a gift as an episode unlock.
- Inventing gift tiers or prices.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "author gift" --graph $GRAPH
```
