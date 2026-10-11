# Stitching UX Experiment

Aliases: stitchingux experiment, story cap renumber

Product context: `content-backend/pfm-kb/modules/stitching-ux.md`

## What it is
Experiment-driven cap and renumber of story lists for stitching UX variants.

## Graph anchors
| `experiment` | `internal/domain/experiments/stitchingux/experiment.go` |
| `GetStories` | `internal/domain/stories/service.go` |

## Risks
- Hard-coding variant caps from memory — read experiment helpers.
- Shipping stitching changes as permanent catalog truth without experiment check.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "experiment" --graph $GRAPH
```
