---
id: flow.radioly-show-details-unlock
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/unlocking/api/handlers/base.py#BasePostHandler
---

**Aliases:** show page, show details, unlock, lock price, open episodes

**When to use:** Show details and unlock for a Pocket FM listener. First stop `BasePostHandler` in `v3/unlocking/api/handlers/base.py`.

**Required inputs:** screen and symptom.
