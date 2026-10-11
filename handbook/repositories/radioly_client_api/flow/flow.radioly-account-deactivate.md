---
id: flow.radioly-account-deactivate
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/user_api/viewsets.py#UserDeactivateRequestView
---

**Aliases:** deactivate account, pause account, deactivate

**When to use:** Listener pauses this login until they sign in again. First stop `UserDeactivateRequestView.deactivate_account`. This is not permanent delete and not forgot-account recovery.

**Required inputs:** login and whether they paused or deleted.
