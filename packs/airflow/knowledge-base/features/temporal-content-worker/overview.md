# Temporal Content Worker

Aliases: content-scheduled-jobs-tasks, content temporal worker

Product context: `airflow/pfm-kb/modules/temporal-content-worker.md`

## What it is
Temporal worker owning content-domain schedules: ranking, daily-show, PPV-related, catalogs, tropes, UGC sync.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `temporal/content/worker.py` | |
| `temporal/content/schedules.py` | |

## Risks
- Editing Airflow DAG when Temporal schedule is live (or reverse).
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Temporal Content Worker" --graph $GRAPH
```
