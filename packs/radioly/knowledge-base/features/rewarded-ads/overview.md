# Rewarded ads

Aliases: rewarded video, watch-an-ad, watch to unlock, earn coins

Product context: `radioly/pfm-kb/modules/rewarded-ads.md`

## What it is

Watch-to-unlock and earn-coins share one product. Completion report
credits; watching does not. Ad-free does not hide this.

## Graph anchors

| Symbol | Source |
|---|---|
| rewarded ads | `v3/ads/rewarded_ads/` |
| `get_rewards_info` | `v3/ads/views.py` |

## Risks

- Paying coins for watch-to-unlock (or unlocking for earn-coins).
- Crediting without a one-time proof.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "get_rewards_info" --graph $GRAPH
```

## Related
- `offerwall`
- `no-ad-pack`
- `in-player-ads`
