---
id: flow.feed-language-cache
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/models.py#fetch_dhf_feed_data
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/models.py#DefaultHomeFeedData
---

Default home-feed cohort cache keys include `{api_type}:{language}:{locale}`
(`fetch_dhf_feed_data`). Spanish shows for English-selected users: inspect
whether the cache key / language passed into DefaultHomeFeedData matches the
user language preference.
