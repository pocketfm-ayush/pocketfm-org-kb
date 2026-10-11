# Temporal Platforms Worker

Aliases: platforms temporal worker

Product context: `airflow/pfm-kb/modules/temporal-platforms-worker.md`

## What it is
Temporal worker for account lifecycle, MoEngage, SendGrid, stories metadata, experiment TTL.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `temporal/platforms/worker.py` | |
| platforms workflows | `temporal/platforms/workflows/` |

## Risks
- Wrong runtime vs classic platform DAGs.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Temporal Platforms Worker" --graph $GRAPH
```
