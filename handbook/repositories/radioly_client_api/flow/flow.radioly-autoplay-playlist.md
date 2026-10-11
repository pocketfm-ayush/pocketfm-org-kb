---
id: flow.radioly-autoplay-playlist
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/feed/views.py#get_playlist_data
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/feed_api/views.py#get_next_recommended_show
---

**Aliases:** playlist, next recommended show, autoplay queue, next up

**When to use:** Autoplay playlist on Pocket FM consumer (radioly). First stop is `get_playlist_data` in `v3/feed/views.py`.

**Required inputs:** screen and symptom.
