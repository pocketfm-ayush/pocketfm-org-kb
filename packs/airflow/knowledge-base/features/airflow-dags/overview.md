# Airflow DAGs and Temporal Jobs

Aliases: airflow jobs, scheduled jobs, temporal workers airflow repo

Product context: `airflow/pfm-kb/modules/scheduled-jobs.md`

## What it is
Pocket FM scheduled and durable backend jobs: catalog freshness, ads mediation
ops, payments recon, experience caches, GenAI/TTS ops, platform plumbing.
Classic Airflow DAGs and Temporal domain workers both live in this repo.

## Graph anchors
| Symbol / area | Source |
|---|---|
| DAG scripts | `dags/` |
| Temporal content workflows | `temporal/content/workflows/` |
| Temporal payments workflows | `temporal/payments/workflows/` |
| Slack alert helpers | `utils/dag_slack_alert.py`, `temporal/common/notify.py` |

## Risks
- Editing the wrong runtime (DAG vs Temporal) leaves the live schedule unchanged.
- Secrets must not be hard-coded.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "What DAG domains and Temporal workflows exist?" --graph $GRAPH
```
