# Account Lifecycle Jobs

Aliases: account deactivation job, account deletion batch, reactivation schedule

Product context: `airflow/pfm-kb/modules/account-lifecycle.md`

## What it is
Scheduled reactivation of expired deactivations and hard-deletion batches for listener accounts.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `UserAccountDeactivationWorkflow` | `temporal/platforms/` / `account_deactivation/` |
| `UserAccountDeletionWorkflow` | same |

## Risks
- Confusing job side effects with in-app delete/deactivate APIs (Radioly).
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Account Lifecycle Jobs" --graph $GRAPH
```
