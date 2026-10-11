# User Default Tab Update

Aliases: user-default-tab-update-worker

Product context: `kafka-stream-clients/pfm-kb/modules/user-default-tab.md`

## What it is
Worker that updates which home tab a user lands on by default based on events/experiments.

## Graph anchors
| `user_default_tab_update_worker` | `workers/user_default_tab_update_worker.py` |

## Risks
- Overwriting user choice without experiment eligibility checks.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "User Default Tab Update" --graph $GRAPH
```
