# Novels Analytics Jobs

Aliases: novel revenue share, fm to novels

Product context: `airflow/pfm-kb/modules/novels-analytics-jobs.md`

## What it is
Novels performance/revenue-share and FM↔novels analytics jobs.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `novels/analytics/` | domain |
| DAGs | `dags/novel_revenue_share_dag.py` |

## Risks
- Inventing revenue-share rates.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Novels Analytics Jobs" --graph $GRAPH
```
