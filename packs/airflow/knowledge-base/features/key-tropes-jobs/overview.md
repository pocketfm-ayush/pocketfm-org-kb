# Key Tropes Jobs

Aliases: key tropes sync, trope mapping seed

Product context: `airflow/pfm-kb/modules/key-tropes-jobs.md`

## What it is
Syncs/seeds trope↔show mappings that power trope discovery.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| Key tropes workflows | `temporal/content/workflows/key_tropes_*.py` |

## Risks
- Inventing trope taxonomies.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Key Tropes Jobs" --graph $GRAPH
```
