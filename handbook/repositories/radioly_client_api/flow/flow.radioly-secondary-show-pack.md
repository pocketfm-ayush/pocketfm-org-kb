---
id: flow.radioly-secondary-show-pack
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/secondary_show_pack/service_manager.py#SecondaryShowPackServiceManager
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/secondary_show_pack/secondary_show_pack_exp/secondary_show_pack_us_exp.py#SecondaryShowPackExperimentUS
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/secondary_show_pack/secondary_show_pack_exp/secondary_show_pack_india_exp.py#SecondaryShowPackExperimentIndia
---

**Aliases:** show coin bundle, unlock this show discount, SSP offer.

**When to use:** Locked player or show page offers a 50%-off coin bundle
for that show, or the usual coin bundles disappeared. US experiment is
checked first, then India. Not My Store. A later refund does not clear the
purchase record or take episodes back. The player ad is impression-capped.

**Required inputs:** UID, show id, locale (US or IN), and the screen.
