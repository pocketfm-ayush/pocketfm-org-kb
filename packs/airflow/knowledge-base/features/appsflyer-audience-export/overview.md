# AppsFlyer Audience Export

Aliases: appsflyer audience import, reactivation appsflyer

Product context: `airflow/pfm-kb/modules/appsflyer-audience-export.md`

## What it is
Exports reactivation/audience cohorts to AppsFlyer for growth campaigns.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `marketing_campaign/appsflyer_audience_import/` | domain |
| reactivation DAGs | `dags/reactivation_sw_*` |

## Risks
- Inventing cohort definitions.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "AppsFlyer Audience Export" --graph $GRAPH
```
