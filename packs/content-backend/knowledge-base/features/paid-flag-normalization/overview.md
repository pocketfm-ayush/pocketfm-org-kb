# Paid Flag Normalization

Aliases: paidnormalization

Product context: `content-backend/pfm-kb/modules/paid-flag-normalization.md`

## What it is
Normalizes the paid flag for eligible series/audiobook contexts so clients do not misread lock state from raw catalog bits.

## Graph anchors
| `Apply` | `internal/domain/features/paidnormalization/service.go` |

## Risks
- Assuming paid=false always means free unlock worldwide.
- Skipping platform eligibility checks.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "Apply" --graph $GRAPH
```
