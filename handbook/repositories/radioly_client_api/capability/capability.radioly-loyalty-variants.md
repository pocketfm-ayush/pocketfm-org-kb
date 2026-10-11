---
id: capability.radioly-loyalty-variants
type: capability
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/gamification/loyalty/experiments/bronze_eligibility_exp/de/constants.py#BronzeEligibilityExpDEConfig
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/gamification/loyalty/experiments/bronze_eligibility_exp/de/exp.py#BronzeEligibilityExpDE
---

**Aliases:** loyalty variants

**When to use:** Locate a variant class in this package. Not the live allocation table and not percentages. Class names: BronzeEligibilityExpDEConfig, BronzeEligibilityExpDEAuralConfig, BronzeEligibilityExpDEIOSConfig, BronzeEligibilityExpDE, BronzeEligibilityExpUKConfig, BronzeEligibilityExpUKAuralConfig, BronzeEligibilityExpUKIOSConfig, BronzeEligibilityExpUK, BronzeEligibilityExpUSConfig, BronzeEligibilityExpUSAuralConfig, BronzeEligibilityExpUSIOSConfig, BronzeEligibilityExpUS, LoyaltyExperimentId, LoyaltyAUNZConfig, LoyaltyAUNZAuralConfig, LoyaltyAUNZConfigIOS, LoyaltyAUNZ, LoyaltyCAConfig, LoyaltyCAAuralConfig, LoyaltyCAConfigIOS, LoyaltyCA, LoyaltyD15ExpDEConfig, LoyaltyD15ExpDEAuralConfig, LoyaltyD15ExpDEIOSConfig, LoyaltyD15ExpDE, LoyaltyD15ExpUKConfig, LoyaltyD15ExpUKAuralConfig, LoyaltyD15ExpUKIOSConfig, LoyaltyD15ExpUK, LoyaltyD15ExpUSConfig, LoyaltyD15ExpUSAuralConfig, LoyaltyD15ExpUSIOSConfig, LoyaltyD15ExpUS, LoyaltyIndiaV5Config, LoyaltyIndiaV5AuralConfig, LoyaltyIndiaV5, LoyaltyIndiaV6Config, LoyaltyIndiaV6AuralConfig, LoyaltyIndiaV6, LoyaltyIndiaV7Config, LoyaltyIndiaV7AuralConfig, LoyaltyIndiaV7, LoyaltyNoDowngradeExpDEConfig, LoyaltyNoDowngradeExpDEAuralConfig, LoyaltyNoDowngradeExpDEIOSConfig, LoyaltyNoDowngradeExpDE, LoyaltyNoDowngradeExpUKConfig, LoyaltyNoDowngradeExpUKAuralConfig, LoyaltyNoDowngradeExpUKIOSConfig, LoyaltyNoDowngradeExpUK, LoyaltyNoDowngradeExpUSConfig, LoyaltyNoDowngradeExpUSAuralConfig, LoyaltyNoDowngradeExpUSIOSConfig, LoyaltyNoDowngradeExpUS, LoyaltyExperimentTemplate.

**Required inputs:** the class name or the listener surface. Cohort rules stay on capability.radioly-experiment-allocation.
