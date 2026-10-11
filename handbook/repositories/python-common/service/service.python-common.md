---
id: service.python-common
type: service
repository: python-common
status: established
evidence:
  - python-common@64749c002b42ec1255b24c1c8e268632249a5f9e:temporal/pfm_temporal/worker.py#run_worker
  - python-common@64749c002b42ec1255b24c1c8e268632249a5f9e:scylla/pfm_scylla/session.py#execute
---

Shared Python packages (`pfm-kafka`, `pfm_scylla`, `pfm_temporal`,
`pfm-logger`) used by Airflow Temporal workers and other Python services.
