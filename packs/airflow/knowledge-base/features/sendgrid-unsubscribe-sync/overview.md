# SendGrid Unsubscribe Sync

Aliases: email unsubscribe sync

Product context: `airflow/pfm-kb/modules/sendgrid-unsubscribe-sync.md`

## What it is
Syncs email unsubscribes so marketing email respects listener preference.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `SendGridUnsubscribeSyncWorkflow` | `temporal/platforms/` |

## Risks
- Confusing with in-app notification permission.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "SendGrid Unsubscribe Sync" --graph $GRAPH
```
