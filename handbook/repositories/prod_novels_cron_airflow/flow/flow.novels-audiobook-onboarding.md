---
id: flow.novels-audiobook-onboarding
type: flow
repository: prod_novels_cron_airflow
status: established
evidence:
  - prod_novels_cron_airflow@af1720b2e08573943b68a2ca2c2b734771177a5f:dags/audiobook_onboarding_v2_dag.py#process_book
  - prod_novels_cron_airflow@af1720b2e08573943b68a2ca2c2b734771177a5f:dags/audiobook_onboarding_v2_dag.py#fetch_book_data
---

Audiobook onboarding DAG tasks (`fetch_book_data` / `process_book`). First
stop for novels audiobook onboarding pipeline failures.
