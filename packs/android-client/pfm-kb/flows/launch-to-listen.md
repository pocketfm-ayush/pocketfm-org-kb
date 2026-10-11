# Launch to listen

## Journey
1. App starts; start/bootstrap classifies onboarding vs logged-in vs guest.
2. Remote Config may select Aural vs legacy shell.
3. Listener reaches home feed (or auth first).
4. Opens a show → player starts; mini player persists.

## Modules
- [aural-vs-legacy](../modules/aural-vs-legacy.md)
- [app-start-and-shell](../modules/app-start-and-shell.md)
- [home-feed-discover](../modules/home-feed-discover.md)
- [show-details](../modules/show-details.md)
- [player](../modules/player.md)

## Failure modes
- Wrong tree edit (legacy vs aural) leaves one segment broken.
- Player AndroidView leak if onRelease omitted.
