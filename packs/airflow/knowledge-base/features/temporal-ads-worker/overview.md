# Temporal Ads Worker

Aliases: ads temporal worker, offerwall temporal

Product context: `airflow/pfm-kb/modules/temporal-ads-worker.md`

## What it is
Temporal worker for ads mediation and offerwall notification schedules.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `temporal/ads/worker.py` | |
| ads workflows | `temporal/ads/workflows/` |

## Risks
- Wrong runtime vs classic ads DAGs.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Temporal Ads Worker" --graph $GRAPH
```
