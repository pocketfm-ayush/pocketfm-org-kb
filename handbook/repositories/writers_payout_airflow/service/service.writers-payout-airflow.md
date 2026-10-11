---
id: service.writers-payout-airflow
type: service
repository: writers_payout_airflow
status: established
evidence:
  - writers_payout_airflow@051ba797a2941ff3adac8fdc2b08bcb4893b3e24:dags/monthly_revenue_share_dag.py#prepare_go_command
---

Writers payout / rewards Airflow DAGs (revenue share, throughput bonus,
nudges). Go workers launched from DAG helpers like `prepare_go_command`.
