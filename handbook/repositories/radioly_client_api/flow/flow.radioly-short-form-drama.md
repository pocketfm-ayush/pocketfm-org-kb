---
id: flow.radioly-short-form-drama
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/short_form_drama/sfd_service_manager.py#SFDServiceManager
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/short_form_drama/experiments/sfd_tv_onsubs_exp.py#SFDTvOnSubsExp
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/short_form_drama/experiments/sfd_tv_onsubs_d0_exp.py#SFDTvOnSubsD0Exp
---

**Aliases:** SFD, TV On Subs, short clips, premium reels, SFDTvOnSubsExp, SFDTvOnSubsD0Exp.

**When to use:** Short-clip locks, SFD paywall copy, or a home reel on a
curated show list. Day-zero is checked first; main TV On Subs is the
fallback. Both share one show list. Main extra gate is Super Saver Pass
rollout, not an active subscription. India and Hindi only. Not a separate
TV app or a second entitlement.

**Required inputs:** show id, locale, language, platform, and subscriber vs
non-subscriber.
