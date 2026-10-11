# ios-client source folder map

| Folder | Product meaning |
|---|---|
| `Pocket FM/Presentation/Features/*` | Listener-facing feature modules (primary twin source) |
| `Pocket FM/Presentation/Navigation` | AppRoutes / route host |
| `Pocket FM/Core` | AppState, DI, analytics helpers |
| `Pocket FM/Domain` + `Data` | Clean-architecture domain/data layers |
| `Pocket FM/CarPlay` | Automotive templates |
| `Pocket FM/Flutter` | Embedded UGC Flutter bridge |
| `Pocket FM/NewDesign` | Transitional UI — confirm before editing |
| `NotificationService*` / `PushTemplateExtension` | Push extensions |
| `PFMStreakLiveActivityWidget` | Streak Live Activity |
| `PocketFmIntents` | App Intents / Siri-related |
| `fastlane/` | Build automation |

Always open `Pocket FM.xcworkspace`. Query graph before inventing ownership.
