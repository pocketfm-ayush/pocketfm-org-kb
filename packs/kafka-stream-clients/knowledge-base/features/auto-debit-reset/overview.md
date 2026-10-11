# Auto Debit Reset Toggle

Aliases: auto-debit-reset-toggle workers

Product context: `kafka-stream-clients/pfm-kb/modules/auto-debit-reset.md`

## What it is
Workers that reset or toggle auto-debit related flags after events/experiments.

## Graph anchors
| `auto_debit_reset_toggle_worker` | `workers/auto_debit_reset_toggle_worker.py` |
| `auto_debit_reset_toggle_worker_v2` | `workers/auto_debit_reset_toggle_worker_v2.py` |

## Risks
- Resetting mandates without payments owner sign-off.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Auto Debit Reset Toggle" --graph $GRAPH
```
