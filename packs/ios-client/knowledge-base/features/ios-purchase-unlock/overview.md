# Purchase and Unlock

Aliases: Purchase funnel, episode unlock, more coins

Product context: `ios-client/pfm-kb/modules/purchase-and-unlock.md`

## What it is
Paywall/unlock flows: episode unlock, purchase funnel, more-coins prompts, and related animations.

## Graph anchors
| `Purchase` | `Pocket FM/Presentation/Features/Purchase` |
| `PFMPurchaseFunnelView` | `Pocket FM/Presentation/Features/Purchase/PFMPurchaseFunnelView` |

## Risks
- Double-charging if unlock retries are not idempotent server-side.
- Confusing NewEpisodeUnlock vs legacy EpisodeUnlock without reading active path.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Purchase and Unlock" --graph $GRAPH
```
