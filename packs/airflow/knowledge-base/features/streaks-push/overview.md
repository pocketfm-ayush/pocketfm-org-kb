# Streaks Push Jobs

Aliases: broken streak push, continuous streak notification

Product context: `airflow/pfm-kb/modules/streaks-push.md`

## What it is
Push jobs that re-engage listeners on broken or continuous listen streaks.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| Streak push workflows | `temporal/experience/` |
| helpers | `feed/utils/fix_streaks.py` |

## Risks
- Inventing streak thresholds.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Streaks Push Jobs" --graph $GRAPH
```
