# Home and Discovery

Aliases: PFMHomeView, top shows, feed modules

Product context: `ios-client/pfm-kb/modules/home-and-discovery.md`

## What it is
Home feed and discovery modules including top-shows style surfaces driven by server widgets/CTAs.

## Graph anchors
| `PFMHomeView` | `Pocket FM/Presentation/Features/PFMHomeView` |
| `PFMTopShowsView` | `Pocket FM/Presentation/Features/PFMTopShowsView` |

## Risks
- Hardcoding layout instead of PFMDS tokens/components.
- Treating Search/KeyTropes/Shorts as the same module as Home.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Home and Discovery" --graph $GRAPH
```
