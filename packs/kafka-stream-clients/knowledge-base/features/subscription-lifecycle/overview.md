# Subscription Lifecycle Workers

Aliases: subscription validation, offer engine, refund handler, subs impression

Product context: `kafka-stream-clients/pfm-kb/modules/subscription-lifecycle.md`

## What it is
Workers for subscription validation, offer engine decisions, refund handling, and subscription impression tracking.

## Graph anchors
| `subscription_validation` | `workers/subscription_validation/` |
| `subscription_offer_engine` | `workers/subscription_offer_engine/` |
| `subscription_refund_handler` | `workers/subscription_refund_handler/` |
| `subs_impression_worker_msk` | `workers/subs_impression_worker_msk.py` |

## Risks
- Changing offer eligibility in workers without product/experiment owners.
- Confusing with iOS/Android StoreKit local state.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Subscription Lifecycle Workers" --graph $GRAPH
```
