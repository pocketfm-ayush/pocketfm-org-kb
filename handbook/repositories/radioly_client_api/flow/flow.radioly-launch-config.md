---
id: flow.radioly-launch-config
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/viewsets.py#LaunchConfigView
---

**Aliases:** launch_config, fetch_config, refresh-config, app launch config, cold start config

**When to use:** Launch Config on Pocket FM consumer (radioly). First stop is `LaunchConfigView` in `v2/feed_api/viewsets.py`.

**Required inputs:** screen and symptom.
