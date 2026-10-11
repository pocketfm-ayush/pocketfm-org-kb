# LiveOps across surfaces

## Journey
1. Device is pre-enrolled for a genre tentpole (supported locale).
2. Launch config may show splash / popup / bottom slider.
3. Home feed may inject billboard, ranked module, and/or mid-feed banner.
4. Discover / autoplay / ads / My Store may show additional touchpoints.
5. Each shown asset records an impression; caps suppress further shows.
6. Episode Zero (sibling) may add show-details promo assets for eligible users.

## Modules
- [liveops-tentpole](../modules/liveops-tentpole.md)
- [launch-config](../modules/launch-config.md)
- [home-feed](../modules/home-feed.md)
- [discover-tab](../modules/discover-tab.md)
- [gtm-impressions](../modules/gtm-impressions.md)
- [my-store](../modules/my-store.md)

## Failure modes
- Missing Fabric asset whitelist → caps do not stick.
- Conflating tentpole with legacy festive → wrong eligibility debugging.
