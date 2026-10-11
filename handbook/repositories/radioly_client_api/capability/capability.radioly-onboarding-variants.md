---
id: capability.radioly-onboarding-variants
type: capability
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/experience/onboarding/experiments/creator_intent_experiment.py#CreatorIntentExperiment
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/experience/onboarding/experiments/genre_onboarding_experiment.py#GenreOnboardingExperiment
---

**Aliases:** onboarding variants

**When to use:** Locate a variant class in this package. Not the live allocation table and not percentages. Class names: CreatorIntentExperiment, GenreOnboardingExperiment, InteractiveOnboardingExperiment, IOSMultiScreenAgeNameRemovalExperiment, NewGenderUIExperiment, SingleScreenOnboardingExperiment, SkipNotificationPermissionExperiment.

**Required inputs:** the class name or the listener surface. Cohort rules stay on capability.radioly-experiment-allocation.
