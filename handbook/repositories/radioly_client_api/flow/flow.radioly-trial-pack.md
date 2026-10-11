---
id: flow.radioly-trial-pack
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/trial_pack_education_ux/service_manager.py#TrialPackServiceManager
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/trial_pack_education_ux/trial_pack_services/plans.py#TrialPackPlansService
---

**Aliases:** starter pack, first coin pack, trial pack education.

**When to use:** A never-payer sees different coin packs on the player, the
offer sheet, launch, or the success message. `TrialPackServiceManager`
picks one pack for that response. Budget Booster and premium compete for
the same slots. A lapsed Budget Booster path goes to My Store, not the
trial sheet. There is no standalone trial screen.

**Required inputs:** UID or device, spending segment if known, and the
surface that disagrees.
