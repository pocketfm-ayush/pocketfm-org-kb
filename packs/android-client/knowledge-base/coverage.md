# android-client pack coverage

**As of:** 2026-09-07 · **Ticket:** FMF-4712

## Source reality
- Dual tree: deprecated `app/` + active `aural/` (~4.5k aural Kotlin files; large legacy tree)
- Graph: ~85k nodes (discovery aid — not a per-symbol encyclopedia in this pack)
- Aural feature families: start, onboarding, home, feed, discover, show, library, player,
  payment, autodebit, ads, streaks, referral, rewards, keytrope, chatbot, share, survey,
  apprating, user, stage, automotive, maintenance, orchestrator, appserverstate, security
- Also: `watch/`, root `security/`, ads helper modules, flutter UGC maven deps

## Pack counts
| Layer | Count |
|---|---|
| Feature overviews | 28 |
| pfm-kb modules | 28 |
| pfm-kb flows | 6 |

## Folder map (product twin status)

| Source area | Status | Twin(s) |
|---|---|---|
| `aural/app`, `aural/start`, `aural/home` | covered | app-start-and-shell, deeplinks |
| `aural/onboarding` | covered | auth-and-onboarding |
| `aural/feed` | covered | home-feed-discover |
| `aural/discover` | covered | discover |
| `aural/library` | covered | library |
| `aural/show` | covered | show-details |
| `aural/player` | covered | player |
| `aural/payment` | covered | payments-and-premium |
| `aural/autodebit` | covered | autodebit |
| `aural/fm-ads-client` | covered | ads |
| `aural/streaks`, `engage` | covered | streaks |
| `aural/referral` | covered | referral |
| `aural/rewards` | covered | rewards |
| `aural/keytrope` | covered | keytrope |
| `aural/chatbot` | covered | chatbot |
| `aural/share` | covered | share |
| `aural/survey` | covered | survey |
| `aural/apprating` | covered | app-rating |
| `aural/user` | covered | user-profile |
| `aural/stage` | covered | stage |
| `aural/automotive` | covered | automotive |
| `aural/maintenance` | covered | maintenance |
| `aural/orchestrator` | covered | orchestrator |
| `aural/appserverstate` | covered | appserver-state |
| `aural/security` + `security/` | covered | device-security |
| `watch/` | covered | watch |
| Dual `app/` vs `aural/` policy | covered | aural-vs-legacy |
| `aural/core/*` | intentional thin | shared infra — CLAUDE + skills |
| Legacy `app/` deep features | intentional thin | bugfix only; not mirrored 1:1 |
| `flutterRepo`, buildSrc, third_party | intentional SKIP | tooling/vendored |

## Intentional SKIP
- Per-Composable / per-ViewModel encyclopedia (use graphify)
- Live Remote Config % and experiment ramps
- Full Radioly feature parity on Android

## Honest gaps
- App-shell coverage ≠ every backend product module
- Always confirm aural vs legacy vs both before edits
- Graph may be stale vs HEAD — compare extract commit
