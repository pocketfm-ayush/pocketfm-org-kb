---
id: flow.radioly-gtm-impressions
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/impression/services/gtm_impression_service.py#GTMImpressionService
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/gtm/services/impression_publisher_service.py#GTMImpressionPublisher
---

**Aliases:** GTM impression, impression publisher, bottom slider impression

**When to use:** GTM Impressions (Radioly publish) on Pocket FM consumer (radioly). First stop is `GTMImpressionService` in `v3/impression/services/gtm_impression_service.py`.

**Required inputs:** screen and symptom.
