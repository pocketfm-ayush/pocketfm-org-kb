---
id: flow.feed-get-feed-data
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/feed_api/views.py#get_feed_data
---

Home feed orchestration. Builds module list (Continue Playing, Popular,
onboarding rails). Suspect for language/locale feed bugs and module ranking
changes. Cache keys for default home feed include `language` and `locale`.
