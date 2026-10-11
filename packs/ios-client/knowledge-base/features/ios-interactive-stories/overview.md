# Interactive Stories

Aliases: PFMInteractiveStories, PFMStories

Product context: `ios-client/pfm-kb/modules/interactive-stories.md`

## What it is
Interactive/branching story experiences and related stories surfaces.

## Graph anchors
| `PFMInteractiveStories` | `Pocket FM/Presentation/Features/PFMInteractiveStories` |
| `PFMStories` | `Pocket FM/Presentation/Features/PFMStories` |

## Risks
- Ignoring branching episode visibility rules that backends/content-backend also enforce.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Interactive Stories" --graph $GRAPH
```
