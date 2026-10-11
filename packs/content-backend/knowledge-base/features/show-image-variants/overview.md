# Show Image Variants

Aliases: designrevamp, resolutionasset, dsthumbnail, mediareplacement

Product context: `content-backend/pfm-kb/modules/show-image-variants.md`

## What it is
Chooses design-revamp, resolution-specific, DS, or experiment media-replacement image URLs for show artwork.

## Graph anchors
| `Eligible` | `internal/domain/features/designrevamp/thumbnail.go` |
| `Eligible` | `internal/domain/features/resolutionasset/image.go` |
| `Apply` | `internal/domain/features/dsthumbnail/thumbnail.go` |
| `assign` | `internal/domain/experiments/mediareplacement/assign.go` |
| `apollo_resolver` | `internal/media/apollo_resolver.go` |

## Risks
- Serving Safari/low-res clients the wrong resolution asset.
- Inventing Apollo media id mappings.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "Eligible" --graph $GRAPH
```
