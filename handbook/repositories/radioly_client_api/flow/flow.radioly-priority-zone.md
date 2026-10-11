---
id: flow.radioly-priority-zone
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/payments/personalised_fast_pass/helpers.py#PriorityZoneHelper
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/payments/personalised_fast_pass/show_zone_info.py#ShowZoneInfoEnricher
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/payments/personalised_fast_pass/banner.py#PFPInlineBanner
---

**Aliases:** early access, finale zone, personalised fast pass, last episodes.

**When to use:** Episode list splits into a free head and a coin-gated tail,
or badges say early access / finale zone. The server computes the split.
Android also needs the experiment. Germany gets the strip, not the player
banner. India Hindi catalog, sleep, and fan-fiction shows are skipped.

**Required inputs:** show id, platform, app version, locale.
