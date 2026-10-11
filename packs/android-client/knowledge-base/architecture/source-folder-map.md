# android-client source folder map

| Folder | Product meaning |
|---|---|
| `aural/` | Active Compose app — prefer for new work |
| `app/` | Deprecated legacy app — bug fixes only unless confirmed |
| `aural/app` | Shell, DI aggregation, navigation destinations |
| `aural/start` | Splash / user-type bootstrap |
| `aural/onboarding` | Auth and first-run |
| `aural/home` + `feed` | Home tabs and explore feed |
| `aural/discover` | Discover widgets |
| `aural/show` | Show details / episodes |
| `aural/library` | Library / bookmarks |
| `aural/player` | Playback, service, mini player |
| `aural/payment` + `autodebit` | Premium, coins, unlock, mandates |
| `aural/fm-ads-client` | Ads / offerwall |
| `aural/streaks` / `rewards` / `referral` | Engage loops |
| `aural/orchestrator` | Cross-module sequences |
| `watch/` | Wear companion |
| `common/`, `network/`, `model/` | Shared legacy/support libraries |

Query graph before inventing module ownership. Confirm aural vs app before editing.
