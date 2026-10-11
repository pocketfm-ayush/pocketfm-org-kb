---
id: flow.feed-continue-playing
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/feed_api/views.py#get_feed_data
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/experience/misc_small_experiments/continue_playing_small_tile_service.py#ContinuePlayingSmallTileService
---

Continue Playing module construction lives in radioly feed
(`get_feed_data` + `ContinuePlayingSmallTileService`). DS may supply ranking
candidates; module assembly for unexpected ranking/content changes starts
here, not on the mobile clients alone.
