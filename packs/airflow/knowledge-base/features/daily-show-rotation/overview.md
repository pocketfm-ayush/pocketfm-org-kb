# Daily Show Rotation

Aliases: dastak rotation, theme show rotation, daily show notification

Product context: `airflow/pfm-kb/modules/daily-show-rotation.md`

## What it is
Rotates theme/daily shows and related notifications so home daily-show surfaces stay current.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `DailyShowRotationWorkflow` | temporal/content |
| `feed/daily_show/` | domain |

## Risks
- Inventing which theme is live today.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Daily Show Rotation" --graph $GRAPH
```
