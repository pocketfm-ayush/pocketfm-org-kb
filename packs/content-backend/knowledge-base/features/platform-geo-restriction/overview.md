# Platform Geo Restriction

Aliases: platformrestriction, GB restrictions

Product context: `content-backend/pfm-kb/modules/platform-geo-restriction.md`

## What it is
Hides or blocks selected shows for specific locale/platform combinations (e.g. GB non-Android).

## Graph anchors
| `IsRestricted` | `internal/domain/features/platformrestriction/service.go` |

## Risks
- Copying restricted show ids into new locales without product/legal review.
- Assuming Android exemption applies everywhere.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "IsRestricted" --graph $GRAPH
```
