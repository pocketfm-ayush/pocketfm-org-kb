---
id: service.android-client
type: service
repository: android_client
status: established
evidence:
  - android_client@f7e1318769a62f83901b7a4accfed287310f4621:aural/player/ui/src/main/java/com/radio/pocketfm/aural/player/ui/screens/PlayerView.kt#PlayerView
  - android_client@f7e1318769a62f83901b7a4accfed287310f4621:aural/app/src/main/java/com/radio/pocketfm/app/di/AppFeatureModule.kt#AppFeatureModule
---

Pocket FM Android app (Aural modules + legacy app/). Owns player UI, show
details episode list, and client-side preference toggles that call radioly
`user.update`.
