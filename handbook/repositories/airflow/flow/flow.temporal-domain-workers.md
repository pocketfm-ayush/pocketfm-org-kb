---
id: flow.temporal-domain-workers
type: flow
repository: airflow
status: established
evidence:
  - airflow@984e6887842e9cf1fe0966626941ff685ac40e12:temporal/platforms/worker.py#main
---

Per-domain Temporal workers (content/ads/payments/experience/genai/platforms)
replace or shadow classic DAGs. First stop for "which Temporal worker owns X".
