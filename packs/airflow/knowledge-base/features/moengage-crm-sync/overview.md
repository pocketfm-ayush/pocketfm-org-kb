# MoEngage CRM Sync

Aliases: moengage catalog, primary show updater, moengage user events

Product context: `airflow/pfm-kb/modules/moengage-crm-sync.md`

## What it is
Keeps MoEngage catalogs, primary-show attributes, and bulk user events aligned with product state.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `MoengagePrimaryShowWorkflow` | `temporal/platforms/` |
| catalogs | `moengage/catalogs/` |

## Risks
- Treating MoEngage sync as in-app notification inbox.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "MoEngage CRM Sync" --graph $GRAPH
```
