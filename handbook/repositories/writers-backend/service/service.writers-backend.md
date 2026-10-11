---
id: service.writers-backend
type: service
repository: writers-backend
status: established
evidence:
  - writers-backend@8bbe0a1e0ab1f7d11aa204236704b3a538522fdf:radioly_api/urls.py#urlpatterns
  - writers-backend@8bbe0a1e0ab1f7d11aa204236704b3a538522fdf:v3/urls.py#urlpatterns
---

Writers / UGC Django backend (content, payments, social, notification). Root
URLConf under `radioly_api` / `v3`. Owns `partner.pocketfm.com` creator
signup via `create_creator_account` / `get_creator_details` — first stop when
a writer cannot create a writer profile or creator ID is missing on CMS
partner flows (cms-dashboard-backend is UI; writers-backend is API).

PagerDuty **`pilot-prod-writers-backend` latency** routes here (writers Django
API), not `ugc-backend` — ugc-backend covers separate UGC-Growth fleet alerts.
