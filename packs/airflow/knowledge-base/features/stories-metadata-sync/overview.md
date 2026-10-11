# Stories Metadata Sync

Aliases: stories metadata workflow

Product context: `airflow/pfm-kb/modules/stories-metadata-sync.md`

## What it is
Refreshes stories metadata used by client/CRM-adjacent surfaces.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `StoriesMetadataWorkflow` | `temporal/platforms/` |

## Risks
- Treating as full catalog CMS.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Stories Metadata Sync" --graph $GRAPH
```
