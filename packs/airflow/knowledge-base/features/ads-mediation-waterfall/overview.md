# Ads Mediation Waterfall

Aliases: mediation groups, waterfall update, avg ecpm job

Product context: `airflow/pfm-kb/modules/ads-mediation-waterfall.md`

## What it is
Creates/updates mediation groups and waterfall/eCPM config so ad fill stays correctly configured.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `CreateMediationGroupsWorkflow` | temporal/ads |
| `UpdateWaterfallWorkflow` | temporal/ads |

## Risks
- Exposing internal mediation IDs as product copy.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Ads Mediation Waterfall" --graph $GRAPH
```
