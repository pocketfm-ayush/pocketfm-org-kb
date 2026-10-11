# Repo Mind — ios_client

Skills + orchestrator must obey this file and `contract.json`. Feature detail lives
in `features/` when present; the code graph lives in `../graphify/graphify-out/`.

**GitHub:** https://github.com/Pocket-Fm/ios_client
**Stack:** Swift · SwiftUI · CocoaPods · SPM · Fastlane

## Purpose

Load `ios-client/pfm-kb/` for product meaning (start at `index.md`).

Pocket FM iOS app. MVVM + Clean Architecture (View → ViewModel → UseCase →
Repository → Service). App-shell twins under `pfm-kb/` — not full Radioly parity.

## Architecture map

| Layer | Location | Owns |
|---|---|---|
| Presentation | `Pocket FM/Presentation/Features/` | SwiftUI + ViewModels (~42 feature folders) |
| Navigation | `Pocket FM/Presentation/Navigation/` | AppRoutes + route host |
| Domain | `Pocket FM/Domain/` | Protocols only |
| Data | `Pocket FM/Data/` | Networking, DTOs, local DB |
| Core | `Pocket FM/Core/` | AppState, DI, analytics |
| CarPlay / Flutter | `CarPlay/`, `Flutter/` | Automotive + UGC embed |
| Extensions | repo-root Notification*/Push*/Live Activity | Push + widgets |

Query the graph before inventing structure:

```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "<question>" --graph $GRAPH
graphify explain "<symbol>" --graph $GRAPH
graphify path "<A>" "<B>" --graph $GRAPH
```

## Conventions

- Always open Pocket FM.xcworkspace, not .xcodeproj.
- New screens: AppRoutes case + getCurrentAppRouteView. Never NavigationLink(destination: SomeView()).
- PFM prefix. Use PFMDS tokens/components — no raw SwiftUI controls when a PFMDS component exists.
- Decoding stays in DataTransferService — never in ViewModels. Domain must not import SwiftUI/UIKit.
- Confirm `Presentation/Features` vs `NewDesign` before editing.
- CODEOWNERS: @Pocket-Fm/iOS-leads.

## Allowed vs protected paths

See `contract.json` → `allowed_edit_paths` / `protected_paths`.
Never write knowledge-base, graphify, env, or secret files.

## External systems & mocking

radioly, content-backend, search, StoreKit/IAP, ads SDKs, Flutter UGC, push providers.

## Commands

```bash
xcodebuild test -workspace "Pocket FM.xcworkspace" -scheme "Pocket FMTests" -destination 'platform=iOS Simulator,name=iPhone 16' -configuration Debug
swiftlint
```

## Rebuild graph

```bash
graphify extract <local-clone> --code-only --out ios-client/graphify
graphify cluster-only ios-client/graphify --no-label
```

## Product context

App-shell product meaning: `ios-client/pfm-kb/` (start at `index.md`).
Code twins: `features/*/overview.md`. Backend behavior: `radioly` / `search` / `content-backend`.

## Coverage

Inventory: `knowledge-base/coverage.md` · folder map: `architecture/source-folder-map.md`.
~35 feature/`pfm-kb` twins covering Presentation features + CarPlay/Flutter/push.
Not a per-ViewModel encyclopedia.

## Gaps

- Deep feature parity with every Radioly module is not mirrored here — shell families.
- `NewDesign/` transitional ownership must be confirmed before treating as source of truth.
- Live prices / Remote Config % are not packed.
