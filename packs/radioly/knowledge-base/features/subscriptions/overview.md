# Subscriptions

Aliases: subscription, premium pass, VIP, cancelled but valid, grace

Product context: `radioly/pfm-kb/modules/subscriptions.md`

## What it is

The pass after pay — not the buy sheet (`paywall`). Cancelled today
is not locked today if still in a valid window. India grace 60 days;
US 30.

## Graph anchors

| Symbol | Source |
|---|---|
| subscriptions | `v3/subscriptions/core/` |

## Risks

- Using one grace number for every market.
- Flipping “subscribed” on the client.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "subscriptions" --graph $GRAPH
```

## Related
- `coin-subscriptions`
- `checkout`
