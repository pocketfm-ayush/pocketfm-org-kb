---
id: flow.radioly-coin-deduct
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/wallet/views.py#deduct_coins
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/wallet/views.py#get_wallet_balances_internal
---

Coins deducted incorrectly / sum of coins spent mismatch / refund my money CS
tickets. Wallet path `deduct_coins` + `get_wallet_balances_internal` — not
pocket_search. Use with `flow.radioly-coin-payment` for payment-failed /
free-coins VOCs.
