# Repo Mind — android_client

Skills + orchestrator must obey this file and `contract.json`. Feature detail lives
in `features/` when present; the code graph lives in `../graphify/graphify-out/`.

**GitHub:** https://github.com/Pocket-Fm/android_client
**Stack:** Kotlin · Gradle · app (legacy) + aural (active)

## Purpose

Load `android-client/pfm-kb/` for product meaning (start at `index.md`).

Pocket FM Android / TV / Auto / Wear. New features go in `/aural/`; `/app/` is
bug-fix only unless confirmed otherwise. Remote Config selects the live path.

## Architecture map

| Layer | Location | Owns |
|---|---|---|
| aural | `aural/` | Active — new features (Compose, clean arch) |
| app | `app/` | Deprecated — bug fixes only |
| watch | `watch/` | Wear companion |
| common/model/network | root libs | Shared support |

Query the graph before inventing structure:

```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "<question>" --graph $GRAPH
graphify explain "<symbol>" --graph $GRAPH
graphify path "<A>" "<B>" --graph $GRAPH
```

## Conventions

- Production APK ships both app and aural; Remote Config picks the flow.
- Confirm aural vs app vs both before every change.
- AndroidView wrapping player surfaces must provide onRelease (DROID-8013).
- Reuse TextHelper / Cta / Media response models — do not duplicate JSON models.
- Reuse PreferenceKeys and AnalyticEventNames — do not invent parallel constants.
- CODEOWNERS: @Pocket-Fm/android.

## Allowed vs protected paths

See `contract.json` → `allowed_edit_paths` / `protected_paths`.
Never write knowledge-base, graphify, env, or secret files.

## External systems & mocking

radioly, content-backend, firebase, payment gateways, ads SDKs.
Confirm app vs aural vs both before editing.

## Commands

```bash
./gradlew test
./gradlew lint
```

## Rebuild graph

```bash
graphify extract <local-clone> --code-only --out android-client/graphify
graphify cluster-only android-client/graphify --no-label
```

## Product context

App-shell product meaning: `android-client/pfm-kb/` (start at `index.md`).
Code twins: `features/*/overview.md`. Prefer aural for new work.
Backend: `radioly` / `search` / `content-backend`.

## Coverage

Inventory: `knowledge-base/coverage.md` · folder map: `architecture/source-folder-map.md`.
~28 feature/`pfm-kb` twins (Aural families + watch/security). Not a per-file encyclopedia.

## Gaps

- Deep feature parity with every Radioly module is not mirrored here — shell + aural families.
- Legacy `app/` is intentionally thin in KB (bug-fix path).
- Live Remote Config % / experiments are not packed.
