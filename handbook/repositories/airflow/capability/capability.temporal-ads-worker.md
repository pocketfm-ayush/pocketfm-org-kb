---
id: capability.temporal-ads-worker
type: capability
repository: airflow
status: established
evidence:
  - airflow@984e6887842e9cf1fe0966626941ff685ac40e12:temporal/ads/worker.py#main
---

Ads Temporal worker entrypoint (`main`) for mediation/ops, offerwall
notifications, DT rewards, eCPM. Catalog `ads` currently points here until a
standalone repo exists.
