# Private Catalog API Auth

Aliases: PrivateAPITokenMW, internal routes, role map

Product context: `content-backend/pfm-kb/modules/private-catalog-api.md`

## What it is
Internal `/internal/*` catalog routes gated by private headers, role tokens, and optional show metadata headers for service-to-service callers.

## Graph anchors
| `PrivateAPITokenMW` | `internal/bootstrap/apiserver/routes.go` |
| `registerInternalRoutes` | `internal/bootstrap/apiserver/routes.go` |

## Risks
- Exposing /internal without role map checks.
- Requiring full PFM client headers on routes that intentionally bypass them.

## Query
```bash
GRAPH=content-backend/graphify/graphify-out/graph.json
graphify explain "PrivateAPITokenMW" --graph $GRAPH
```
