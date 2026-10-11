---
id: flow.radioly-auto-debit
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/content_api/auto_debit/constants.py#AutoDebitV4Enum
---

**Aliases:** auto debit, auto unlock, manage auto-unlock

**When to use:** Auto-unlock for a Pocket FM listener. First stop `AutoDebitV4Enum` in `v2/content_api/auto_debit/constants.py`.

**Required inputs:** screen and symptom.
