# App Start and Shell

Aliases: PocketActivity, AppRoot, start bootstrap, home host

Product context: `android-client/pfm-kb/modules/app-start-and-shell.md`

## What it is
Aural app entry, splash/start user-type resolution, bottom navigation host, and top-level DI/navigation wiring.

## Graph anchors
| `AppFeatureModule` | `aural/app/.../di/AppFeatureModule.kt` |
| `PocketActivity / AppRoot` | `aural/app/` |
| `start getUserType` | `aural/start/` |

## Risks
- Adding destinations outside FMNavigationDestination / HomeNavigationDestination sealed roots.
- Duplicating preference/analytics constants outside PreferenceKeys / AnalyticEventNames.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "App Start and Shell" --graph $GRAPH
```
