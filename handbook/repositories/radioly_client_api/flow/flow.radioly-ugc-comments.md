---
id: flow.radioly-ugc-comments
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/social/views.py#get_ugc_comments
---

Internal UGC comments API `v3/content/internal/get_ugc_comments` (fm-content-pvt)
lives in radioly `get_ugc_comments` — use for username freshness / stale mongo
name bugfixes on that path (not content-backend).
