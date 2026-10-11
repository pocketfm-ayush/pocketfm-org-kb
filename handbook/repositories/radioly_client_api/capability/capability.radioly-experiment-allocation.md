---
id: capability.radioly-experiment-allocation
type: capability
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/experiments/base_experiment_class.py#BaseExperimentClass
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/experiments/new_payment_journey/base.py#NewPaymentJourneyBase
---

**Aliases:** running experiments, experiment inventory, EXPERIMENT_ID, which experiment, A/B allocation, experiment bucketing, variant, experiment id.

**When to use:** Any “which experiment / which variant” ask for Pocket FM
consumer. Allocation is server-owned (`BaseExperimentClass.allocate_variant`).
Payments variants are assigned in `v3/payments/experiments`; what the variant
changes lives in the feature flow (payment journey, trial pack, short-form
drama, and the rest). Do not answer from the old radioly pack note.

**Required inputs:** symptom plus locale, platform, and logged-in vs guest
when the cohort matters. Do not invent live percentages, winners, or
experiment ids.

Control must not see treatment. A payment screen must not re-allocate a
cohort launch already owns. A missing personalised plan ranking falls back
to the default order. Wound-down coin-education credits can still appear in
coin history as a bonus or a Pocket FM gift.
