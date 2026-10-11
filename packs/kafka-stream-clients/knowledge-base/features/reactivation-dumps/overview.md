# Reactivation Audience Dumps

Aliases: inactive-user MoEngage S3 dump

Product context: `kafka-stream-clients/pfm-kb/modules/reactivation-dumps.md`

## What it is
Workers that dump inactive/reactivation cohorts (e.g. to S3) for MoEngage/growth reactivation.

## Graph anchors
| `reactivation/s3_dump` | `workers/reactivation/` |

## Risks
- Inventing cohort definitions.
- Confusing with Airflow AppsFlyer audience export.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Reactivation Audience Dumps" --graph $GRAPH
```
