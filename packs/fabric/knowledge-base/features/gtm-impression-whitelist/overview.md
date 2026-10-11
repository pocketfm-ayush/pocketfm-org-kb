# GTM Asset Whitelist

Aliases: gtm_whitelist_config, FM/novels/comics/TV asset allowlists

Product context: `fabric/pfm-kb/modules/gtm-asset-whitelist.md`

## What it is
Per-tenant allowlists of GTM asset types that the impression consumer will store; unknown assets are skipped.

## Graph anchors
| `isWhitelistedGTMAsset` | `impression/server/consumer/gtm_whitelist_config.go` |
| `initFMAssets` | `impression/server/consumer/gtm_whitelist_config.go` |

## Risks
- Adding a new marketing surface without updating the whitelist.
- Copying FM whitelist to novels/comics/TV without checking tenant maps.

## Query
```bash
GRAPH=fabric/graphify/graphify-out/graph.json
graphify query "GTM Asset Whitelist" --graph $GRAPH
```
