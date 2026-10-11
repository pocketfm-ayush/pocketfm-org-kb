---
id: flow.radioly-coin-payment
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/payments/views.py#get_wallet_balances_internal
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/payments/services/payment_validation_popup_service.py#get_transaction_failed_message
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/my_store/services/my_store_services.py#get_free_coins_banner_details
---

Coin / wallet payment CS tickets ("please check this ticket", Freshdesk VOC:
payment failed, payment showing failed, coins not credited, coins deducted
incorrectly, refund my money, daily free coins / giveaway). Own in radioly
payments + wallet (`deduct_coins`, `get_wallet_balances_internal`,
`get_transaction_failed_message`, `get_free_coins_banner_details`). Channel
`#pocket-toons-cs` often posts UID-only — expand VOC for coins/payment/refund
before content-backend/ugc.
