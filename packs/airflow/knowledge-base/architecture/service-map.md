# Airflow pack — service map

| Runtime | Location | Role |
|---|---|---|
| Airflow DAGs | `dags/` | Scheduled batch still on Airflow UI (prod←main, dev←develop) |
| Temporal workers | `temporal/<domain>/` | Migrated durable jobs: content, ads, payments, experience, genai, platforms |

Do not assume a DAG is gone because a Temporal domain exists — verify both.
Secrets via secret manager helpers only.
