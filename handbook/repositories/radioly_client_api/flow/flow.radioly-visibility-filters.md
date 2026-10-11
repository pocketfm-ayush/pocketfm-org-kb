---
id: flow.radioly-visibility-filters
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/helpers.py#filter_disabled_shows_from_feed
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/helpers.py#filter_hidden_shows_from_feed
---

**Aliases:** disabled shows, hidden shows, campaign-only, campaign PGC

**When to use:** Home visibility filters on Pocket FM consumer (radioly). First stop is `filter_disabled_shows_from_feed` in `v2/feed_api/helpers.py`.

**Required inputs:** screen and symptom.
