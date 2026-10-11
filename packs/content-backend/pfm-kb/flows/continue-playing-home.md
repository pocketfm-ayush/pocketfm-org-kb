# Continue Playing on home

## Journey
1. Experience/home caller asks for Continue Playing candidates for a user/device/profile.
2. Service loads onboarding + recent play snapshot.
3. Geo/removed filters apply; active vs stale ranking is produced.
4. BFF renders Continue Playing using ranked items.

## Modules
- [home-continue-playing-slices](../modules/home-continue-playing-slices.md)
- [private-catalog-api](../modules/private-catalog-api.md)

## Failure modes
- Missing upstream play state → empty or thin CP.
- Geo restriction removes titles without a user-facing error from this API.
