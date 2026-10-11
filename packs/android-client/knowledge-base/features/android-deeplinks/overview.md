# Deeplinks and Navigation

Aliases: FMNavigationDestination, HomeDeeplink, deep links

Product context: `android-client/pfm-kb/modules/deeplinks.md`

## What it is
App-root and home-graph destinations plus deeplink routing into tabs/features.

## Graph anchors
| `FMNavigationDestination` | `aural/app/.../FMNavigationDestination.kt` |
| `HomeNavigationDestination` | `aural/app/.../HomeNavigationDestination.kt` |
| `HomeDeeplink` | `aural/app/.../HomeDeeplink.kt` |

## Risks
- Inventing string routes instead of sealed destinations.
- Handling GCD deeplinks without checking content-backend attribution storage when relevant.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Deeplinks and Navigation" --graph $GRAPH
```
