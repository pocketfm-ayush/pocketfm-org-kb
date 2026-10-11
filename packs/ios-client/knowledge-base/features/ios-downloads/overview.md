# Downloads

Aliases: PFMDownloadView, offline episodes

Product context: `ios-client/pfm-kb/modules/downloads.md`

## What it is
Offline download management UI for episodes saved to device.

## Graph anchors
| `PFMDownloadView` | `Pocket FM/Presentation/Features/PFMDownloadView` |

## Risks
- Assuming downloaded content bypasses all entitlement checks forever.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Downloads" --graph $GRAPH
```
