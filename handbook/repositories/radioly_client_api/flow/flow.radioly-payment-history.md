---
id: flow.radioly-payment-history
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/history/services/eligibility.py#PaymentHistoryEligibilityService
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/history/views/coins_history.py#CoinsHistoryView
---

**Aliases:** history, coins history, purchase history, transaction receipt

**When to use:** Payment history on Pocket FM consumer (radioly). First stop is `PaymentHistoryEligibilityService` in `v3/history/services/eligibility.py`.

**Required inputs:** screen and symptom.
