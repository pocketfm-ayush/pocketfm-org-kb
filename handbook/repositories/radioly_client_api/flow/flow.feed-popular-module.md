---
id: flow.feed-popular-module
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/feed_constants/modules.py#POPULAR_MODULE_ID
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/recommendation_helpers.py#ShowPopularityRecommendation
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/services/feed/module_processor.py#get_localized_module_title
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/constants.py#LocalizedText
---

Popular on Pocket FM module composition (`POPULAR_MODULE_ID` /
`long_series_module_id`) is assembled in radioly
(`ShowPopularityRecommendation`). Module title string
`LocalizedText.POPULAR_ON_POCKET_FM_MODULE_LABEL` ("Popular on Pocket FM") is
localized by `ModuleProcessorService.get_localized_module_title` — first stop
when UI shows "Pocketfm" instead of "Pocket FM" in the home module title, or
Top 10 Ranking not visible after Nth show in horizontal list (API has data).
LATAM/Italian Popular locale filtering also lives here.

**Split ownership:** module title / ranking / locale filtering → **radioly**
(this entity). Open **content-backend** only when the bug is show-catalog /
payload composition after radioly module assembly is ruled out (not for
branding string typos).

