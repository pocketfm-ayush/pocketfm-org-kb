# Show Unlocks and Battle Pass

Aliases: battlepass unlock worker, show unlocks scylla, device show status

Product context: `kafka-stream-clients/pfm-kb/modules/show-unlocks-and-battle-pass.md`

## What it is
Workers that materialize show unlock entitlements including battle-pass unlocks and device-show status updates.

## Graph anchors
| `battle_pass_user_show_unlock` | `workers/battle_pass_user_show_unlock/` |
| `device_show_status` | `workers/device_show_status/` |
| `show_unlocks_scylla` | `workers/show_unlocks_scylla.py` |

## Risks
- Assuming request-time unlock API alone is source of truth without these workers.
- MSK vs non-MSK consumer drift.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Show Unlocks and Battle Pass" --graph $GRAPH
```
