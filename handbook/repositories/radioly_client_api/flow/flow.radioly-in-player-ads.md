---
id: flow.radioly-in-player-ads
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/ads/ads_cms/viewsets.py#AdsViewSet
---

**Aliases:** mid-roll, instream, virtual voice ahead, disclaimer ad, boundary audio

**When to use:** In-player ads for a Pocket FM listener. First stop `AdsViewSet` in `v3/ads/ads_cms/viewsets.py`.

**Required inputs:** screen and symptom.
