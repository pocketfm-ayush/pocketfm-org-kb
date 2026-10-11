# Surveys

Aliases: in-app surveys

Product context: `android-client/pfm-kb/modules/survey.md`

## What it is
In-app survey prompts and response capture.

## Graph anchors
| `survey ui` | `aural/survey/ui` |
| `survey domain` | `aural/survey/domain` |

## Risks
- Treating surveys as permanent settings screens.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Surveys" --graph $GRAPH
```
