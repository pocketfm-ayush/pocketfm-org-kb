# Open app with launch config

## Journey
1. Listener opens or refreshes the app.
2. Client fetches launch config.
3. Server may read Nexus segments / IAM identity as needed and allocate experiments.
4. Config enables feature flags, promos (including Budget Booster / GTM hooks), and player sampling.
5. Home and other surfaces load under that config.

## Modules
- [launch-config](../modules/launch-config.md)
- [experiments-allocation](../modules/experiments-allocation.md)
- [nexus-user-profile](../modules/nexus-user-profile.md)
- [budget-booster](../modules/budget-booster.md)
- [gtm-impressions](../modules/gtm-impressions.md)

## Failure modes
- Config timeout → client uses degraded/defaults (client-specific).
- Wrong segment from Nexus → mistargeted paywall/ads intensity.
