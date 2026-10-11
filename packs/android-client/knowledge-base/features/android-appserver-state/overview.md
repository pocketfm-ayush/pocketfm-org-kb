# App Server State

Aliases: appserverstate, server-driven app state

Product context: `android-client/pfm-kb/modules/appserver-state.md`

## What it is
Client packaging of server-driven app state used to coordinate UI/feature availability.

## Graph anchors
| `appserverstate data` | `aural/appserverstate/data` |
| `APP_SERVER_STATE docs` | `APP_SERVER_STATE_ARCHITECTURE.md` |

## Risks
- Treating appserver state as a second preference store for arbitrary keys.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "App Server State" --graph $GRAPH
```
