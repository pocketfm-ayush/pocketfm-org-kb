# Offerwall Reward Ops

Aliases: tapjoy failed reward, digital turbine failed reward, ow coins earned

Product context: `airflow/pfm-kb/modules/offerwall-reward-ops.md`

## What it is
Offerwall earned-coin notifications and failed-reward recovery for Tapjoy/DT/Adjoe-style partners.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `OwCoinsEarnedNotificationWorkflow` | temporal/ads |
| Failed reward workflows | temporal/ads |

## Risks
- Inventing live task lists or exchange rates.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Offerwall Reward Ops" --graph $GRAPH
```
