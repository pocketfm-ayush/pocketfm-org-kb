# Premium Management

Aliases: ManageSubscription, premium welcome/cancel

Product context: `ios-client/pfm-kb/modules/premium-manage.md`

## What it is
Manage, pause, cancel, and welcome surfaces for premium subscriptions.

## Graph anchors
| `Premium` | `Pocket FM/Presentation/Features/Premium` |
| `managePremiumSubscription route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Implementing cancel copy that contradicts App Store subscription management rules.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Premium Management" --graph $GRAPH
```
