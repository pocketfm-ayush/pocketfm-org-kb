# Meta Audience Sync

Aliases: meta/audience_v*, Facebook Custom Audiences

Product context: `airflow/pfm-kb/modules/meta-audience-sync.md`

## What it is
Jobs that sync/build Meta (Facebook) custom audiences used for ads targeting.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `meta/audience_v*` | `meta/` |
| `export_facebook_campaign_data` | `marketing_campaign/` |

## Risks
- Inventing audience definitions.
- Hard-coding Meta API secrets.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Meta Audience Sync" --graph $GRAPH
```
