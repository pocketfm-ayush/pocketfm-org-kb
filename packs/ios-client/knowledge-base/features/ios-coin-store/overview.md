# Coin Store

Aliases: PFMStoreView, coin packs, about coins

Product context: `ios-client/pfm-kb/modules/coin-store.md`

## What it is
Coin pack store UI, banners, and related coin education/history entry points.

## Graph anchors
| `PFMStoreView` | `Pocket FM/Presentation/Features/PFMStoreView` |
| `coinHistory route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |
| `PFMHistory` | `Pocket FM/Presentation/Features/PFMHistory` |

## Risks
- Hardcoding pack prices that StoreKit/backend return.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Coin Store" --graph $GRAPH
```
