# ios-client pack coverage

**As of:** 2026-09-07 · **Ticket:** FMF-4712

## Source reality
- SwiftUI app under `Pocket FM/` with ~42 Presentation/Features folders
- Extensions: NotificationService*, PushTemplateExtension, Streak Live Activity, Intents
- Also: CarPlay, Flutter UGC embed, NewDesign transitional tree, Core/Data/Domain layers
- Graph present (~74MB) — discovery aid, not per-symbol encyclopedia in this pack

## Pack counts
| Layer | Count |
|---|---|
| Feature overviews | 35 |
| pfm-kb modules | 35 |
| pfm-kb flows | 6 |

## Folder map (product twin status)

| Source area | Status | Twin(s) |
|---|---|---|
| `Presentation/Navigation`, `PFMBaseView`, `PFMLandingView`, Core AppState | covered | app-shell-and-navigation, deeplinks |
| `PFMOnboardingView` | covered | auth-and-onboarding |
| `PFMHomeView`, `PFMTopShowsView` | covered | home-and-discovery |
| `PFMSearchView` | covered | search |
| `PFMLibraryView`, `PFMSavedEpView` | covered | library |
| `PFMShowDetail` | covered | show-details |
| `PFMPlayerView`, play widgets | covered | player |
| `PFMDownloadView` | covered | downloads |
| `PFMAudioBook` | covered | audiobook |
| `PFMStoreView`, `Purchase`, `Premium`, `PFMPremiumSubscription` | covered | payments-and-premium, coin-store, purchase-and-unlock, premium-manage |
| `AutoDebit` | covered | autodebit |
| `PFMStreaks` + Live Activity ext | covered | streaks |
| `Loyalty` | covered | loyalty |
| `PFMRewardedVideo`, `PFMDailyLoginReward` | covered | rewards-and-ads |
| `PFMKeyTropes` | covered | keytropes |
| `UserViews` | covered | user-profile |
| `PFMCommentView`, `PFMReviewView` | covered | comments-and-reviews |
| `AuthorProfile`, gifting, author note | covered | author-and-gifting |
| `PFMUgcOriginal`, `Flutter/` | covered | ugc-flutter |
| `PFMSpaceView` | covered | space |
| `PFMSleepStories` | covered | sleep-stories |
| `PFMInteractiveStories`, `PFMStories` | covered | interactive-stories |
| `PFMDiscoverShortsTab` | covered | discover-shorts |
| `InAppSurvey`, `PFMCSAT` | covered | survey-and-csat |
| `PFMAppRatingView` | covered | app-rating |
| `GDPRConsent` | covered | gdpr-consent |
| `CarPlay/` | covered | carplay |
| Notification/Push extensions | covered | push-notifications |
| `GenericWebView` | covered | generic-webview |
| `Admin Controls` | covered | admin-controls |
| AI character chat routes | covered | ai-character-chat |
| `PFMHistory` | covered via coin-store | coin history / transactions |
| `Domain/`, `Data/`, `Core/` infra | intentional thin | architecture — CLAUDE + Docs |
| `NewDesign/` | intentional thin | transitional — confirm before treating as source of truth |
| `Pocket FMTests`, UITests, fastlane | intentional SKIP | harness/tooling |
| Third-party xcframeworks | intentional SKIP | vendored |

## Intentional SKIP
- Per-ViewModel encyclopedia (use graphify)
- Live StoreKit prices / Remote Config %
- Full Radioly feature parity on iOS

## Honest gaps
- App-shell coverage ≠ every backend product module
- Always use xcworkspace; confirm NewDesign vs Features path before edits
- Graph may be stale vs HEAD — compare extract commit
