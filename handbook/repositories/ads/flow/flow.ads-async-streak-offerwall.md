---
id: flow.ads-async-streak-offerwall
type: flow
repository: ads
status: uncertain
evidence:
  - airflow@984e6887842e9cf1fe0966626941ff685ac40e12:temporal/ads/worker.py#main
  - airflow@984e6887842e9cf1fe0966626941ff685ac40e12:temporal/ads/workflows/pocket_saga_offerwall_rename.py#PocketSagaOfferwallRenameWorkflow
  - airflow@984e6887842e9cf1fe0966626941ff685ac40e12:temporal/ads/workflows/create_mediation_groups.py#CreateMediationGroupsWorkflow
---

Async ads side effects: Temporal ads worker entry (`main` in
`temporal/ads/worker.py`), offerwall rename (`PocketSagaOfferwallRenameWorkflow`),
and AdMob mediation group sync (`CreateMediationGroupsWorkflow`).
