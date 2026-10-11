# English Description Preference

Aliases: englishdescdrop

Product context: `content-backend/pfm-kb/modules/english-description.md`

## What it is
Prefers English description fields when the actor content language is English.

## Graph anchors
| `Apply` | `internal/domain/features/englishdescdrop/service.go` |

## Risks
- Dropping localized descriptions for non-English content_ln.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "Apply" --graph $GRAPH
```
