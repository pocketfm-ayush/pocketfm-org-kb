# Payments and Premium

Aliases: subscriptions, coins, unlock, Juspay, wallet

Product context: `android-client/pfm-kb/modules/payments-and-premium.md`

## What it is
Subscriptions, coin wallet, unlocking, and payment UI including Juspay gateway integration in Aural payment modules.

## Graph anchors
| `payment ui` | `aural/payment/ui` |
| `payment domain` | `aural/payment/domain` |
| `DeductCoinOrchestrator` | `aural/orchestrator/` |

## Risks
- Duplicating payment success/failure models already in shared model packages.
- Changing unlock UX without checking coin orchestrator sequencing.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Payments and Premium" --graph $GRAPH
```
