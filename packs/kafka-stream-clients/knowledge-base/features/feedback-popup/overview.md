# Feedback Popup Worker

Aliases: feedback-popup-worker-v2

Product context: `kafka-stream-clients/pfm-kb/modules/feedback-popup.md`

## What it is
Worker that processes feedback-popup eligibility or response events asynchronously.

## Graph anchors
| `feedback_popup_worker_v2` | `workers/feedback_popup_worker_v2.py` |

## Risks
- Prompting every session — eligibility is gated.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Feedback Popup Worker" --graph $GRAPH
```
