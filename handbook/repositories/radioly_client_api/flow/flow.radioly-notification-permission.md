---
id: flow.radioly-notification-permission
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/push_notification/views.py#get_notification_data
---

**Aliases:** enable notifications, notification sheet, push opt-in

**When to use:** Notification permission prompts on Pocket FM consumer (radioly). First stop is `get_notification_data` in `v2/push_notification/views.py`.

**Required inputs:** screen and symptom.
