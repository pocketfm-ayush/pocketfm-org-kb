# Aural vs Legacy App Paths

Aliases: aural vs app, Remote Config dual APK

Product context: `android-client/pfm-kb/modules/aural-vs-legacy.md`

## What it is
Production APK ships both legacy `app/` and active `aural/`; Firebase Remote Config chooses which flow a user sees. New features belong in aural unless confirmed otherwise.

## Graph anchors
| `CLAUDE module scope` | `CLAUDE.md` |
| `aural CLAUDE` | `aural/CLAUDE.md` |

## Risks
- Shipping new features only in legacy `app/` without confirmation.
- Assuming a bug fix in one path covers both user segments.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Aural vs Legacy App Paths" --graph $GRAPH
```
