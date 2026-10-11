# Temporal Payments Worker

Aliases: payments temporal worker, recon temporal

Product context: `airflow/pfm-kb/modules/temporal-payments-worker.md`

## What it is
Temporal worker for recon, passes, unlocks, loyalty pushes, EU churn, coin ops.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `temporal/payments/worker.py` | |
| payments workflows | `temporal/payments/workflows/` |

## Risks
- Wrong runtime vs classic payments DAGs.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Temporal Payments Worker" --graph $GRAPH
```
