---
id: flow.writers-creator-signup
type: flow
repository: writers-backend
status: established
evidence:
  - writers-backend@8bbe0a1e0ab1f7d11aa204236704b3a538522fdf:v2/user_api/views.py#create_creator_account
  - writers-backend@8bbe0a1e0ab1f7d11aa204236704b3a538522fdf:v2/user_api/views.py#get_creator_details
---

partner.pocketfm.com writer/creator profile creation. `create_creator_account`
and `get_creator_details` own signup failures and missing creator ID for
writers. CMS may surface the bug; API ownership is writers-backend (not
content-backend / radioly).
