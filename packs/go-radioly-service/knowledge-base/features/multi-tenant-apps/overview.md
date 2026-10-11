# Multi-Tenant Apps

Aliases: FM Comics Novels TV product tenants

Product context: `go-radioly-service/pfm-kb/modules/multi-tenant-apps.md`

## What it is
Relay serves multiple Pocket product apps (FM, Comics, Novels, TV) with tenant-aware routing, headers, and exporter topics.

## Graph anchors
| `routeFM` | `internal/eventrouter/router.go` |
| `routeComics` | `internal/eventrouter/router.go` |
| `product.Product` | `go-common enum usage` |

## Risks
- Copying FM-only handler rules to Comics/TV without checking route* branches.
- Ignoring app version pin files as product truth.

## Query
```bash
GRAPH=go-radioly-service/graphify/graphify-out/graph.json
graphify explain "routeFM" --graph $GRAPH
```
