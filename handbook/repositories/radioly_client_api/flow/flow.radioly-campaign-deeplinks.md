---
id: flow.radioly-campaign-deeplinks
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/content_api/ad_helpers.py#AdsetEntityHelper
---

**Aliases:** campaign deeplink, ad deeplink, install deeplink, open from campaign

**When to use:** A campaign or install link that resolves to a show or story and can open it playing. First stop `AdsetEntityHelper.get_adset_entity_show_id`. Not trailer-code, not a launch-overlay link, and not a Discover share pin. An unmapped id is a miss.

**Required inputs:** campaign or ad-set id and the show or story it opened.
