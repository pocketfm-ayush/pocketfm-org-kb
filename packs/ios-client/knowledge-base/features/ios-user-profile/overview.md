# User Profile and Settings

Aliases: UserViews, account settings, multi-profile

Product context: `ios-client/pfm-kb/modules/user-profile.md`

## What it is
Profile, settings, followers, multi-profile manage/create/edit, and related account screens.

## Graph anchors
| `UserViews` | `Pocket FM/Presentation/Features/UserViews` |
| `accountSettings route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |
| `manageProfile route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Implementing delete-account without confirming backend/legal flow.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "User Profile and Settings" --graph $GRAPH
```
