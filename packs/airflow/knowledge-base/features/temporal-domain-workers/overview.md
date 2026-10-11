# Temporal Domain Workers (Airflow repo)

Aliases: temporal content worker, temporal payments worker

Product context: `airflow/pfm-kb/modules/temporal-domain-workers.md`

## What it is
Durable Temporal workers under `temporal/` domains (content, ads, payments,
experience, genai, platforms). Migration target away from classic DAGs.

## Graph anchors
| Area | Source |
|---|---|
| content worker | `temporal/content/worker.py` |
| payments workflows | `temporal/payments/workflows/` |
