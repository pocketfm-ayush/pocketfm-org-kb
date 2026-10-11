# Auto Debit

Aliases: AutoDebit feature, auto unlock manager

Product context: `ios-client/pfm-kb/modules/autodebit.md`

## What it is
Auto-debit / auto-unlock management for recurring payment preferences.

## Graph anchors
| `AutoDebit` | `Pocket FM/Presentation/Features/AutoDebit` |
| `showAutoUnlockManagerView route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Treating autodebit as a one-time coin purchase.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Auto Debit" --graph $GRAPH
```
