# Deeplink open

## Journey
1. External link/push/GCD deeplink arrives.
2. Navigation destinations route to home/show/payment/etc.
3. Attribution storage may be consulted for deferred installs.

## Modules
- [deeplinks](../modules/deeplinks.md)
- [app-start-and-shell](../modules/app-start-and-shell.md)
- [show-details](../modules/show-details.md)

## Failure modes
- Unknown destination drops to home silently.
- Deferred deeplink TTL expired in attribution store.
