# Loyalty Rewards

Aliases: Loyalty, loyaltyRewardsView

Product context: `ios-client/pfm-kb/modules/loyalty.md`

## What it is
Loyalty rewards program UI for long-term listener benefits.

## Graph anchors
| `Loyalty` | `Pocket FM/Presentation/Features/Loyalty` |
| `loyaltyRewardsView route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Merging loyalty with daily-login or offerwall without checking product owners.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Loyalty Rewards" --graph $GRAPH
```
