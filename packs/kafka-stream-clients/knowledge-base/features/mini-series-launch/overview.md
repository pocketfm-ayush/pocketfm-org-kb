# Mini Series Launch Worker

Aliases: mini-series-show-launch

Product context: `kafka-stream-clients/pfm-kb/modules/mini-series-launch.md`

## What it is
Worker that handles mini-series show launch side effects when launch events fire.

## Graph anchors
| `mini_series_launch_worker` | `workers/mini_series_launch_worker.py` |

## Risks
- Launching without confirming CMS publish state.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Mini Series Launch Worker" --graph $GRAPH
```
