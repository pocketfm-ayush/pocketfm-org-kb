# GCD deeplink resolve

## Journey
1. Attribution pipeline upserts an AppsFlyer GCD deeplink for a device.
2. Later experience flow reads or patches the record within TTL.
3. Deeplink drives deferred deep navigation.

## Modules
- [attribution-deeplink-storage](../modules/attribution-deeplink-storage.md)
- [private-catalog-api](../modules/private-catalog-api.md)

## Failure modes
- TTL expiry → not found; caller must handle missing deeplink.
- Wrong service confused with Relay cookie attribution store.
