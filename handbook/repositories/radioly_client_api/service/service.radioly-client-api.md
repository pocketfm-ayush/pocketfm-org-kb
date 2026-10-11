---
id: service.radioly-client-api
type: service
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/feed_api/views.py#get_feed_data
---

Primary Pocket FM Django API (radioly). Production home feed traffic hits
`get_feed_data` (v3 implementation served under v2 URL). First stop for
feed, unlock, user, Credit Space, and content bugs owned by the client-api /
feed TG — including `#going_live` Credit Space / audiobook launch PRs under
`Pocket-Fm/radioly_client_api`.
