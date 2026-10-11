# Deeplink open

## Journey
1. Push/campaign/UGC link arrives.
2. Notification extension may decorate payload.
3. AppRoutes (or Flutter UGC bridge) opens the destination.

## Modules
- [deeplinks](../modules/deeplinks.md)
- [push-notifications](../modules/push-notifications.md)
- [ugc-flutter](../modules/ugc-flutter.md)
- [app-shell-and-navigation](../modules/app-shell-and-navigation.md)

## Failure modes
- Unknown route drops silently.
- Flutter bridge mismatch for UGC destinations.
