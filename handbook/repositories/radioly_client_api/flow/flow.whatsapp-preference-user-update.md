---
id: flow.whatsapp-preference-user-update
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/user_api/views.py#update_users
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/user_api/views.py#_store_whatsapp_preference
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:external_services/iam/constants.py#ENDPOINTS
---

WhatsApp notification toggle does not persist after refresh: primary ownership
is radioly + IAM, not the Android/iOS UI toggle alone. Client API
`POST /v2/user_api/user.update` (`update_users`) accepts `is_whatsapp` and
persists via `_store_whatsapp_preference` → UsersMeta props. Profile fields on
the same call go to IAM `PUT /v1/profile` (`ENDPOINTS["UPDATE_PROFILE"]`).
Debug order: radioly `user.update` first, then IAM `is_whatsapp` /
`UpdateProfile`.
