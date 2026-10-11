# Stage

Aliases: stage feature modules

Product context: `android-client/pfm-kb/modules/stage.md`

## What it is
Stage product surface (domain/data/ui) for stage-specific listening/content experiences.

## Graph anchors
| `stage ui` | `aural/stage/ui` |
| `stage domain` | `aural/stage/domain` |

## Risks
- Assuming Stage is identical to Show details.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Stage" --graph $GRAPH
```
