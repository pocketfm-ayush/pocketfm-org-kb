---
id: flow.radioly-app-rating-popup
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/feed_api/services/helper.py#is_in_app_review_eligible
---

**Aliases:** rate the app, app rating, in-app review, store rating sheet

**When to use:** Server gate for the rate-Pocket-FM sheet. First stop `is_in_app_review_eligible`. Not the player-minimise survey and not support ticket rating.

**Required inputs:** device and whether the sheet showed, was skipped, or was rated.
