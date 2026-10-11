# App Shell and Navigation

Aliases: AppRoutes, AppState, base shell, landing

Product context: `ios-client/pfm-kb/modules/app-shell-and-navigation.md`

## What it is
Route-based navigation shell (`AppRoutes` + path arrays), base chrome, landing/bootstrap surfaces, and DI container wiring.

## Graph anchors
| `AppRoutes` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |
| `PFMBaseView` | `Pocket FM/Presentation/Features/PFMBaseView` |
| `PFMLandingView` | `Pocket FM/Presentation/Features/PFMLandingView` |
| `AppState` | `Pocket FM/Core/AppState` |

## Risks
- Using NavigationLink(destination:) instead of AppRoutes + getCurrentAppRouteView.
- Putting decoding/network calls in ViewModels.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "App Shell and Navigation" --graph $GRAPH
```
