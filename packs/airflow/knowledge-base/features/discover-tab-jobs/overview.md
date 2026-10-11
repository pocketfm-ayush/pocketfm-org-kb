# Discover Tab Jobs

Aliases: discover metadata sync, shorts upload dag

Product context: `airflow/pfm-kb/modules/discover-tab-jobs.md`

## What it is
Syncs Discover/shorts metadata and related media so Discover stays fresh.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| discover sync | `experience/discover_tab/` |
| DAGs | `dags/sync_discovery_show_metadata_dag.py` |

## Risks
- Inventing Discover rail order.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Discover Tab Jobs" --graph $GRAPH
```
