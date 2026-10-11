# Catalog Sync Jobs

Aliases: top50 catalog, new release catalog, discovery metadata

Product context: `airflow/pfm-kb/modules/catalog-sync-jobs.md`

## What it is
Maintains top/new-release/discovery catalogs used by feed and CRM.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| Catalog workflows | `temporal/content/` |

## Risks
- Treating as full CMS write path.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Catalog Sync Jobs" --graph $GRAPH
```
