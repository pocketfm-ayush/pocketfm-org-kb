---
id: flow.radioly-coin-subscriptions
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/coin_subscriptions/impression_service.py#CoinSubImpressionService
---

**Aliases:** coin subscription, auto-renewing coin pack

**When to use:** Coin pack subscriptions for a Pocket FM listener. First stop `CoinSubImpressionService` in `v3/payments/coin_subscriptions/impression_service.py`.

**Required inputs:** screen and symptom.
