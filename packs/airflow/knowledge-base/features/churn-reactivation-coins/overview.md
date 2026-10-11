# Churn Reactivation Coins

Aliases: churn coin credit, reactivation coins

Product context: `airflow/pfm-kb/modules/churn-reactivation-coins.md`

## What it is
Credits coins for churn-reactivation campaigns so returning listeners receive promised grants.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| churn coin credit service | `churn_reactivation/` |
| DAG | `dags/churn_reactivation_coin_credit_dag.py` |

## Risks
- Inventing coin amounts or live campaign windows.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Churn Reactivation Coins" --graph $GRAPH
```
