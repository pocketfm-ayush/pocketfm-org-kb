---
id: flow.radioly-account-delete
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/user_api/apps.py#UserApiConfig
---

**Aliases:** delete account, close account, account deletion

**When to use:** Account delete for a Pocket FM listener. First stop `UserApiConfig` in `v2/user_api/apps.py`.

**Required inputs:** screen and symptom.
