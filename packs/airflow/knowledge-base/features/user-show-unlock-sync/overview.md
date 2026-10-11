# User Show Unlock Sync

Aliases: unlock sync job, unordered unlock patch

Product context: `airflow/pfm-kb/modules/user-show-unlock-sync.md`

## What it is
Syncs show unlock state so paid/unlocked access matches what listeners expect after purchases.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `UserShowUnlockSyncWorkflow` | temporal/payments |
| `unlocking/` | domain helpers |

## Risks
- Changing unlock UX rules here — Radioly owns request-time unlock.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "User Show Unlock Sync" --graph $GRAPH
```
