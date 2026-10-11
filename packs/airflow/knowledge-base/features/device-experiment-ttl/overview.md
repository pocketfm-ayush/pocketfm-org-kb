# Device Experiment TTL Refresh

Aliases: experiment ttl refresh

Product context: `airflow/pfm-kb/modules/device-experiment-ttl.md`

## What it is
Refreshes device experiment TTLs so long-lived allocations do not expire incorrectly.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `DeviceExperimentTTLRefreshWorkflow` | `temporal/platforms/` |

## Risks
- Inventing live allocation percentages.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Device Experiment TTL Refresh" --graph $GRAPH
```
