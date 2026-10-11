# VIP Binge Super Saver Jobs

Aliases: vip expiry, binge pass expiry, super saver daily

Product context: `airflow/pfm-kb/modules/vip-binge-super-saver.md`

## What it is
Pass/VIP lifecycle jobs: expiry, pre-expiry, and Super Saver daily maintenance affecting entitlements.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `VipExpiredUsersWorkflow` | temporal/payments |
| Binge/SuperSaver workflows | temporal/payments / payments/ |

## Risks
- Inventing pass prices or grace windows.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "VIP Binge Super Saver Jobs" --graph $GRAPH
```
