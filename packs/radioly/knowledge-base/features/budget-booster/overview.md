# Budget Booster Deal (BBD)

Aliases: budget booster, BBD, flash sale pack, rush offer, cyclic coin deal

Product context: `radioly/pfm-kb/modules/budget-booster.md`

## What it is
Personalized limited-time coin packs with boosted bonus, injected into My Store,
payment options, player, and launch GTM surfaces — not a standalone destination.
Implemented under `v3/budget_booster/`.

## Graph anchors
| Symbol | Source |
|---|---|
| `BBDHandler` | `v3/budget_booster/handler.py` |
| Budget booster package | `v3/budget_booster/` |


## Key product notes

Personalized limited-time coin packs with boosted bonus coins. Injected into
My Store, payment options, player, and launch promo surfaces — not a standalone
tab. Pack assignment is sticky for the current sale/cycle window.

## Risks
- Sticky pack per sale window — do not reshuffle mid-window from segment drift.
- Event/flash outrank cyclic when both eligible.
- Live prices/windows are volatile — do not pack them.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "BBDHandler" --graph $GRAPH
```

## Related
- `my-store`
- `checkout`
- `launch-config`
