# Bigger Thumbnails Jobs

Aliases: BT editorial allocation, bigger thumbnails campaign

Product context: `airflow/pfm-kb/modules/bigger-thumbnails-jobs.md`

## What it is
Allocates editorial bigger-thumbnail treatments and orchestrates BT CMS campaigns for home art.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `AllocateBtEditorialWorkflow` | temporal/experience |
| `experience/bigger_thumbnails/` | domain |

## Risks
- Confusing with retired top-shows smart caching.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Bigger Thumbnails Jobs" --graph $GRAPH
```
