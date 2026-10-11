# Paywall

Aliases: buy sheet, coin wall, unlock sheet

Product context: `radioly/pfm-kb/modules/paywall.md`

## What it is
Client-facing buy / unlock sheet orchestration and eligibility — not My Store catalog itself.

## Graph anchors
| Paywall / unlock sheet services | CODE SEARCH under payments + content unlock |
| Related | `checkout`, `my-store`, `pricing`, `coins-wallet` |


## Key product notes

The sheet the listener sees when they hit a lock: what they can buy or
watch-an-ad for. The **server** chooses the sheet and the plans from which
screen they came from.

## Risks
- Inventing coin prices (volatile).
- Conflating paywall sheet with checkout PG routing.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "Paywall" --graph $GRAPH
```

## Related
- `checkout`
- `coins-wallet`
- `pricing`
