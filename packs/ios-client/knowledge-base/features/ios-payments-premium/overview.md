# Payments and Premium

Aliases: store, premium subscription, purchase funnel umbrella

Product context: `ios-client/pfm-kb/modules/payments-and-premium.md`

## What it is
Umbrella for coin store, premium subscription, and purchase/unlock monetization entry points on iOS.

## Graph anchors
| `PFMStoreView` | `Pocket FM/Presentation/Features/PFMStoreView` |
| `PFMPremiumSubscription` | `Pocket FM/Presentation/Features/PFMPremiumSubscription` |
| `Purchase` | `Pocket FM/Presentation/Features/Purchase` |
| `Premium` | `Pocket FM/Presentation/Features/Premium` |

## Risks
- Logging payment secrets or raw gateway payloads.
- Skipping StoreKit/receipt verification paths.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Payments and Premium" --graph $GRAPH
```
