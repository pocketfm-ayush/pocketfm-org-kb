---
id: flow.radioly-web-checkout-bonus
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/experiments/web_bonus_tier/exp.py#get_web_bonus_tier_percentage
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/experiments/web_payment_route/exp.py#WebPaymentRouteExp
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/web_commissions/models.py#UserWebCommissionMeta
---

**Aliases:** web coin bonus, pay on web extra coins, iOS web sheet.

**When to use:** Extra coins for paying on the web, or an iOS US web-checkout
sheet. Not the default App Store or Play checkout. India is excluded. The
bonus steps down after repeated successful web purchases
(`get_web_bonus_tier_percentage`). Refunds do not decrement
`UserWebCommissionMeta` web count. Web count and in-app count are separate.
There is no listener screen for the ledger.

**Required inputs:** UID, locale, platform, and whether the charge was web
or in-app.
