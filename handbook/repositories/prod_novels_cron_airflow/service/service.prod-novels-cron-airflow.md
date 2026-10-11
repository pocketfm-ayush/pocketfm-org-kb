---
id: service.prod-novels-cron-airflow
type: service
repository: prod_novels_cron_airflow
status: established
evidence:
  - prod_novels_cron_airflow@af1720b2e08573943b68a2ca2c2b734771177a5f:dags/audiobook_onboarding_v2_dag.py#process_book
---

Novels/UGC production Airflow DAG fleet (onboarding, plagiarism, audio
mastering, withdrawals). Separate from Pocket FM `airflow` Temporal monorepo.
