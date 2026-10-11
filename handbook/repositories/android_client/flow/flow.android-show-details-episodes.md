---
id: flow.android-show-details-episodes
type: flow
repository: android_client
status: established
evidence:
  - android_client@f7e1318769a62f83901b7a4accfed287310f4621:app/src/main/java/com/radio/pocketfm/app/showDetail/EpisodeViewBinder.kt#EpisodeViewBinder
  - android_client@f7e1318769a62f83901b7a4accfed287310f4621:aural/appserverstate/data/src/main/java/com/radio/pocketfm/aural/appserverstate/data/AppServerStateManager.kt#AppServerStateManager
---

Show-details episode list binding (`EpisodeViewBinder`) plus app server state.
When Resume Episode disagrees with unlocked count, radioly
`_get_clamped_start_index` owns the pointer; Android only displays the clamped
value — do not rank android_client above radioly for that bug class.
