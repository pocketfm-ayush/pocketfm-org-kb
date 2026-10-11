---
id: flow.radioly-player-feed
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/feed_api/views.py#get_player_feed
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/feed_api/views.py#get_player_feed_new
---

**Aliases:** player feed, player rails, episode page feed, get_player_feed, next series, new releases, new on pocketfm

**When to use:** Player feed on Pocket FM consumer (radioly). First stop is `get_player_feed` in `v3/feed_api/views.py`.

**Required inputs:** screen and symptom.
