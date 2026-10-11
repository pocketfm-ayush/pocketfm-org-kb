---
id: flow.unlock-orchestrator
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/unlocking/service/orchestrator.py#unlock
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/unlocking/api/views.py#unlock_state_view
---

Episode unlock orchestration (`unlock` / `unlock_smart`) and unlock-state API.
Use for unlock-count vs resume mismatches after confirming clamp in
`_get_clamped_start_index`, and for "listened to all episodes but still shows
not listened / not getting the DU" unlock-state bugs (pair with ads/apollo
only after radioly unlock path is ruled out).
