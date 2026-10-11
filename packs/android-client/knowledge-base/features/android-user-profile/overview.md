# User Profile and Settings

Aliases: profile, settings, account management

Product context: `android-client/pfm-kb/modules/user-profile.md`

## What it is
Profile, settings, and account management under the Aural user module.

## Graph anchors
| `user ui` | `aural/user/ui` |
| `user domain` | `aural/user/domain` |

## Risks
- Storing new preference keys outside PreferenceKeys.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "User Profile and Settings" --graph $GRAPH
```
