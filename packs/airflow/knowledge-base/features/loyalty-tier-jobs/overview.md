# Loyalty Tier Jobs

Aliases: loyalty playtime coin spent, loyalty pro expiry push

Product context: `airflow/pfm-kb/modules/loyalty-tier-jobs.md`

## What it is
Aggregates loyalty playtime/spend and sends Pro expiry / active-week style pushes.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `loyalty_tier_program/` | domain |
| Loyalty push workflows | temporal/payments or experience |

## Risks
- Inventing tier thresholds.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Loyalty Tier Jobs" --graph $GRAPH
```
