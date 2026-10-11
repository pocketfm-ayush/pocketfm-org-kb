# Auto Debit

Aliases: autodebit payment features

Product context: `android-client/pfm-kb/modules/autodebit.md`

## What it is
Auto-debit enrollment and management surfaces sitting beside core payment flows.

## Graph anchors
| `autodebit ui` | `aural/autodebit/ui` |
| `autodebit domain` | `aural/autodebit/domain` |

## Risks
- Treating autodebit as identical to one-time coin purchase UX.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Auto Debit" --graph $GRAPH
```
