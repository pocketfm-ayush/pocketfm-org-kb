---
id: capability.episode-seq-number
type: capability
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/content_api/models.py#Stories
---

Episode `seq_number` is owned on the Stories model in radioly content_api.
Production seq_number / episode ordering bugs and related PR lineage start
in `radioly_client_api` (Stories + unlock/resume paths that write seq).
