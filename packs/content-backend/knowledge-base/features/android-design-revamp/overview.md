# Android Design Revamp Experiment

Aliases: androiddesignrevamp

Product context: `content-backend/pfm-kb/modules/android-design-revamp.md`

## What it is
Experiment gate used with design-revamp image selection for eligible Android clients.

## Graph anchors
| `experiment` | `internal/domain/experiments/androiddesignrevamp/experiment.go` |
| `Eligible` | `internal/domain/features/designrevamp/thumbnail.go` |

## Risks
- Applying Android-only revamp art to iOS/web without eligibility checks.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "experiment" --graph $GRAPH
```
