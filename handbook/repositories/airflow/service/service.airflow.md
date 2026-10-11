---
id: service.airflow
type: service
repository: airflow
status: established
evidence:
  - airflow@984e6887842e9cf1fe0966626941ff685ac40e12:temporal/platforms/worker.py#main
---

Pocket FM scheduled-jobs monorepo: classic Airflow DAGs (`dags/`) plus Temporal
domain workers under `temporal/`. Confirm DAG vs Temporal runtime before
owning a job.
