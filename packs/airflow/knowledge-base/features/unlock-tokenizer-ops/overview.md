# Unlock Tokenizer Ops

Aliases: unlocking/ tokenizer unlock patch, unlock job tracker

Product context: `airflow/pfm-kb/modules/unlock-tokenizer-ops.md`

## What it is
Unlocking maintenance jobs (tokenizer unlock patches, unlock job tracker cleanup) supporting paid-access correctness.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `tokenize_unlock_patch` | `unlocking/tokenize_unlock_patch.py` |
| `unlock_job_tracker_cleanup` | `unlocking/unlock_job_tracker_cleanup.py` |

## Risks
- Running unlock patches without reconciling with user-show-unlock-sync.
- Treating alerts as user-facing unlock API.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Unlock Tokenizer Ops" --graph $GRAPH
```
