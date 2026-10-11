# Experience Scheduled Jobs

Aliases: experience dags, experience temporal

Product context: `airflow/pfm-kb/modules/experience-scheduled-jobs.md`

## What it is
Umbrella for experience-domain schedules: streaks, referral, Discover, BT, reengage, loyalty pushes.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `experience/` | domain |
| `temporal/experience/` | |

## Risks
- Too coarse alone — prefer specific twins when debugging one surface.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Experience Scheduled Jobs" --graph $GRAPH
```
