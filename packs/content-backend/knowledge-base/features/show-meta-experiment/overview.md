# Show Meta Experiment

Aliases: showmeta experiment

Product context: `content-backend/pfm-kb/modules/show-meta-experiment.md`

## What it is
Experiment hooks that can alter show metadata presentation for assigned variants.

## Graph anchors
| `experiment` | `internal/domain/experiments/showmeta/experiment.go` |

## Risks
- Baking experiment payloads into permanent CMS fields.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "experiment" --graph $GRAPH
```
