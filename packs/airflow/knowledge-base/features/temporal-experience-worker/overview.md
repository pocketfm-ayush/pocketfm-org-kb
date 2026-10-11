# Temporal Experience Worker

Aliases: experience temporal worker

Product context: `airflow/pfm-kb/modules/temporal-experience-worker.md`

## What it is
Temporal worker for streaks, referral, story evolution, chatbot eligibility, reengage caches.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `temporal/experience/worker.py` | |
| experience workflows | `temporal/experience/workflows/` |

## Risks
- Wrong runtime vs classic experience DAGs.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Temporal Experience Worker" --graph $GRAPH
```
