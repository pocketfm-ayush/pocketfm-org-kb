# Episode coin pricing

Aliases: billing pricing, coins required, episode price

Product context: `radioly/pfm-kb/modules/pricing.md`

## What it is

Internal “what does this episode cost in coins for this listener?”
Must match the show page. Not a shop. Paywall owns the sheet.

## Graph anchors

| Symbol | Source |
|---|---|
| pricing | `v3/pricing/` |


## Key product notes

Internal “what does this episode cost in coins for this listener?”
Not a shop the listener opens. Must match the show page.

Paywall still owns the sheet. Subscriptions own the pass.

## Risks

- A price that disagrees with show-open.
- Inventing coins, plan IDs, or experiment splits.
- Battle-pass titles may not match — treat as open.

## Related
- `paywall`
- `checkout`
- `rule_engine (ops HarperCollins)`

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "pricing" --graph $GRAPH
```
