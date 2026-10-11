---
id: flow.search-request
type: flow
repository: pocket_search
status: established
evidence:
  - pocket_search@c4b23df2fca4de1bb6be59e13bb3fd54328e96ab:v3/search/views.py#build_response
  - pocket_search@c4b23df2fca4de1bb6be59e13bb3fd54328e96ab:v3/search/views.py#UniversalSearchV3Handler
---

Search request orchestration via `UniversalSearchV3Handler.build_response`.
First stop for ranking/empty-results bugs on universal search and
`fm-search-prod` / fm-search PagerDuty fires.
