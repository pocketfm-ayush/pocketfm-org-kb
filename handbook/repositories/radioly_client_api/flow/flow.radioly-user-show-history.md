---
id: flow.radioly-user-show-history
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/user_api/viewsets.py#UserShowHistoryView
---

**Aliases:** show.history, user.show.history, UserShowHistoryView, listening history

**When to use:** User show history API on Pocket FM consumer (radioly). First stop is `UserShowHistoryView` in `v2/user_api/viewsets.py`.

**Required inputs:** screen and symptom.
