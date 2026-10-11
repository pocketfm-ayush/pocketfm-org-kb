# S2S Attribution Jobs

Aliases: purchase s2s dag, s2s mismatch detector, activation s2s

Product context: `airflow/pfm-kb/modules/s2s-attribution-jobs.md`

## What it is
Scheduled purchase/activation/watch S2S events and mismatch detection for growth attribution.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `s2s_events/` | domain code |
| DAGs | `dags/purchase_s2s_events_dag.py`, `dags/s2s_mismatch_detector_dag.py` |

## Risks
- Overlapping ownership with Relay / kafka S2S workers — verify path.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "S2S Attribution Jobs" --graph $GRAPH
```
