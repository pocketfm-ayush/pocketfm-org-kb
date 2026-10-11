---
id: flow.radioly-listening-progress
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/user_api/playtime_helpers.py#CassandraUserShowPlaytimeService
---

**Aliases:** resume, last listened, playtime progress

**When to use:** Listening progress for a Pocket FM listener. First stop `CassandraUserShowPlaytimeService` in `v2/user_api/playtime_helpers.py`.

**Required inputs:** screen and symptom.
