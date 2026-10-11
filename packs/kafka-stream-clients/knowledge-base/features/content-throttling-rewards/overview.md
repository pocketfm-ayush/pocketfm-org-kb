# Content Throttling Rewards

Aliases: content-throttling-v2 daily throttling reward

Product context: `kafka-stream-clients/pfm-kb/modules/content-throttling-rewards.md`

## What it is
Worker that processes daily content-throttling reward events for eligible listening/throttling programs.

## Graph anchors
| `content_throttling_v2` | `workers/content_throttling_v2/` |

## Risks
- Confusing with Airflow content-throttling scheduled jobs.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Content Throttling Rewards" --graph $GRAPH
```
