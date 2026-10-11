---
id: flow.radioly-airtel-premium
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/integrations/airtel/services.py#PromotionService
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/integrations/airtel/services.py#AirtelOrderService
---

**Aliases:** airtel premium, airtel claim, carrier premium, Airtel free subscription

**When to use:** Carrier-granted Premium. Airtel creates the order (`AirtelOrderService`); the listener claims it on the Pocket FM page (`PromotionService.claim`). Not a store buy and not Reward Club. One successful claim per login. Window length is `AIRTEL_FREE_DAYS` in code; do not invent a price.

**Required inputs:** order id, login, and whether claim was eligible.
