# Branching Stories

Aliases: branching domain feature

Product context: `content-backend/pfm-kb/modules/branching-stories.md`

## What it is
Show-specific story list reshaping for branching narrative products (phase caps / alternate endings style cuts).

## Graph anchors
| `Apply` | `internal/domain/features/branching/branching.go` |

## Risks
- Applying branching cuts to arbitrary shows without allowlisted show ids.
- Confusing branching with stitching experiment caps.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "Apply" --graph $GRAPH
```
