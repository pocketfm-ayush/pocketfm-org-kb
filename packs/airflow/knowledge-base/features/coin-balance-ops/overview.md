# Coin Balance Ops

Aliases: bulk coin credit, coin balance update job

Product context: `airflow/pfm-kb/modules/coin-balance-ops.md`

## What it is
Batch coin balance updates and bulk credits for wallet correctness.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `BulkCoinCreditWorkflow` | `temporal/payments/workflows/bulk_coin_credit.py` |
| Coin balance update | temporal/payments |

## Risks
- Inventing credit amounts.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Coin Balance Ops" --graph $GRAPH
```
