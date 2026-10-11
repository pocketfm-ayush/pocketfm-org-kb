# Re-engage Rewards Redis

Aliases: reengage rewards cache job

Product context: `airflow/pfm-kb/modules/reengage-rewards-redis.md`

## What it is
Refreshes re-engage reward eligibility caches so reward surfaces stay correct.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `ReengageRewardsRedisWorkflow` | `temporal/experience/` |

## Risks
- Confusing with Radioly rewards API request path.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Re-engage Rewards Redis" --graph $GRAPH
```
