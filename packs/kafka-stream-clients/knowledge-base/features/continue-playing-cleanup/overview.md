# Continue Playing Cleanup

Aliases: continue-playing-show-deletion worker

Product context: `kafka-stream-clients/pfm-kb/modules/continue-playing-cleanup.md`

## What it is
Worker that removes or cleans Continue Playing entries when shows should no longer appear.

## Graph anchors
| `continue_playing_show_deletion` | `workers/continue_playing_show_deletion.py` |

## Risks
- Deleting CP state that content-backend still expects.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Continue Playing Cleanup" --graph $GRAPH
```
