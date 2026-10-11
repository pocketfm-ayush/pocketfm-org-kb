# Auto-unlock

Aliases: auto debit, auto unlock, manage auto-unlock

Product context: `radioly/pfm-kb/modules/auto-debit.md`

## What it is
Per-series **keep unlocking while listening** using wallet balance. Not
subscription auto-renew and not the paywall sheet. Distinct from unlocking
byline (labels only).

## Graph anchors
| Symbol | Source |
|---|---|
| Auto debit services | `v2/content_api/auto_debit/` and/or `v3/experience/auto_debit/` (verify both) |
| `AutoDebitToggleService` | content auto_debit package |

## Key edges
- Requires coins / unlock pricing (`pricing`, `coins-wallet`).
- Manage list can be empty without being an error.
- Show-details-unlock owns open counts; auto-debit keeps extending them.

## Risks
- Calling this “subscription auto-renew.”
- Changing byline copy when auto-debit toggle is the real ask.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify explain "AutoDebitToggleService" --graph $GRAPH
```
