---
id: flow.resume-pointer-clamp
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/content_api/models.py#_get_clamped_start_index
---

Show details Resume Episode is higher than unlocked episode count: owning
repo/file/function is radioly `v2/content_api/models.py#_get_clamped_start_index`
(not android_client first). It clamps the start/resume index so "Resume
Episode N" cannot exceed unlocked count. After radioly, verify client display
of the returned pointer (android_client / ios_client).
