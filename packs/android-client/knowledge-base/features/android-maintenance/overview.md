# Maintenance Mode

Aliases: app down, maintenance UI

Product context: `android-client/pfm-kb/modules/maintenance.md`

## What it is
Maintenance / app-down UI when backend signals the app should block normal browsing.

## Graph anchors
| `maintenance ui` | `aural/maintenance/ui` |
| `AppDownConfig` | `aural/start/...` |

## Risks
- Hardcoding maintenance copy that server config should supply.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Maintenance Mode" --graph $GRAPH
```
