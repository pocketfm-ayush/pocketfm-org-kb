# Facebook Campaign Insights Export

Aliases: facebook_insights, marketing_campaign reports

Product context: `airflow/pfm-kb/modules/facebook-campaign-insights.md`

## What it is
Exports Facebook campaign/insights style data for growth reporting and AppsFlyer-adjacent marketing pipelines.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `facebook_insights.py` | `marketing_campaign/facebook_insights.py` |
| `s2s_events_report_new.py` | `marketing_campaign/s2s_events_report_new.py` |

## Risks
- Treating insights export as real-time Relay S2S delivery.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Facebook Campaign Insights Export" --graph $GRAPH
```
