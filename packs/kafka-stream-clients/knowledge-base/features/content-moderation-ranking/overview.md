# Content Moderation / Comment Ranking

Aliases: dscommentranker, spam comments

Product context: `kafka-stream-clients/pfm-kb/modules/content-moderation-ranking.md`

## What it is
Workers that rank or filter comments (DS comment ranker) and related spam-comment handling.

## Graph anchors
| `ds_comment_ranking` | `workers/content/ds_comment_ranking.py` |
| `spam_comments` | `workers/spam_comments/` |

## Risks
- Auto-hiding comments without moderation policy review.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Content Moderation / Comment Ranking" --graph $GRAPH
```
