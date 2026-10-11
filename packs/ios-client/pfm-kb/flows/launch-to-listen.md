# Launch to listen

## Journey
1. App launches into shell/landing and auth gates as needed.
2. Listener reaches home discovery.
3. Opens show details and starts player.
4. Playback continues with mini player / background session.

## Modules
- [app-shell-and-navigation](../modules/app-shell-and-navigation.md)
- [auth-and-onboarding](../modules/auth-and-onboarding.md)
- [home-and-discovery](../modules/home-and-discovery.md)
- [show-details](../modules/show-details.md)
- [player](../modules/player.md)

## Failure modes
- Route not registered in AppRoutes → dead navigation.
- Auth/GDPR gate loops prevent home.
