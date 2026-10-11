# Content Throttling Jobs

Aliases: content throttling migration, throttled shows

Product context: `airflow/pfm-kb/modules/content-throttling-jobs.md`

## What it is
Jobs that migrate/notify around throttled shows affecting listener access pacing.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `content_throttling/` | domain |
| related DAGs | `dags/content_throttling_*` |

## Risks
- Inventing throttle windows.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Content Throttling Jobs" --graph $GRAPH
```
