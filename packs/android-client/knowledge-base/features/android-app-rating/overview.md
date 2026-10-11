# App Rating

Aliases: in-app rating dialogs

Product context: `android-client/pfm-kb/modules/app-rating.md`

## What it is
In-app rating prompt flows that ask satisfied listeners to rate the app.

## Graph anchors
| `apprating ui` | `aural/apprating/ui` |
| `apprating domain` | `aural/apprating/domain` |

## Risks
- Prompting on every session — eligibility is gated.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "App Rating" --graph $GRAPH
```
