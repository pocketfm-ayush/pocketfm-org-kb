---
id: service.pocket-search
type: service
repository: pocket_search
status: established
evidence:
  - pocket_search@c4b23df2fca4de1bb6be59e13bb3fd54328e96ab:v3/search/views.py#UniversalSearchV3View
---

Pocket Search Django service (`fm-search` / `pocket_search` / `FM-Search`).
Universal search v3 entry view `UniversalSearchV3View`. First stop for
PagerDuty `fm-search-prod` / `[FIRING] fm-search-prod` / search TG latency and
empty-results ranking bugs — not radioly or IAM.
