---
id: capability.radioly-subscription-variants
type: capability
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/subscriptions/biz_models/super_saver_pass/experiments/billboard_final_rollout.py#FinalRolloutBillboard
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/subscriptions/biz_models/super_saver_pass/experiments/billing_grace_period.py#BillingGracePeriodExperiment
---

**Aliases:** subscription variants

**When to use:** Locate a variant class in this package. Not the live allocation table and not percentages. Class names: FinalRolloutBillboard, BillingGracePeriodExperiment, BingerFreeAppExp, CoinPackOnThresholdExp, DEPUK, DEPD0UK, DEPIT, DEPD0IT, DEPExperimentNewDesigns, DEPAssetsUSNoVideo, DEPExperimentNewDesignsUS, SbmDepD15PaidAssetsNoVideo, SBMDEPM0USAssetNoVideo, SBMDEPD0US, SbmDepD0FreeTrialAssetsNoVideo, SBMDEPD0FreeTrialUS, SbmDepD15US, SBMDEPM0USAssetD30NoVideo, SBMDEPD30US, DEPM0USAssetNoVideo, SBMDEPUS, MHPDEPUK, DepV4UsAssetNoVideo, DepV4Exp, DepV4ExpM2, DEPM0USMonthly, DEPM0USMonthlyNonCampaign, EarlyPaywallExperiment, PocketSubscriptionReverseAB, PremiumAdoptionExp, PremiumAdoptionExpNew, AssetsINNoVideo, PocketSubscriptionReverseABNewPlans, PocketSubscriptionReverseABCampaign, FinalRolloutDirectPurchase, FinalRolloutPremiumV2, M1AnnualPlansExp, M1MonthlyPlansExpAssetsNoVideo, ThreeDayFreeTrialWithoutMandateExp, VideoOnMystoreExp, FinalRolloutPremiumD15, PlanLinkFlowExp, NudgeUserRePurchaseExp, OneTapRenewPauseExp, FinalRolloutPremiumV2GSTPricingExp, M0FreeTrialINExp, FreePlusGoldExpPlans, FreePlusGoldShowPremiumUserCohortEnum, FreePlusGoldExpAssets, FreePlusGoldShowPremium, FreePlusGoldShowPremiumUserCohort, SSPFreeCatalogueExperiment, ActiveSubsAudioTrialInternalAdService, M0AnnualCampaignSubsInternalAdService, M0AnnualCampaignSubsUSInternalAdService, M0PPVSubsForUSusersInternalAdService, LapsedOptimizedAssetNoVideo, LapsedPricingOptimizationExp, build_show_lookup_dicts, M0AnnualCampaignSubs. Plus 59 more classes in the same package.

**Required inputs:** the class name or the listener surface. Cohort rules stay on capability.radioly-experiment-allocation.
