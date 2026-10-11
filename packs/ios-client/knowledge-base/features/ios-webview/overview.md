# Generic WebView

Aliases: GenericWebView, purchase webview

Product context: `ios-client/pfm-kb/modules/generic-webview.md`

## What it is
In-app web views for generic URLs and some purchase/web checkout flows.

## Graph anchors
| `GenericWebView` | `Pocket FM/Presentation/Features/GenericWebView` |
| `PurchaseWebView` | `Pocket FM/Presentation/Features/Purchase/PurchaseWebView` |

## Risks
- Loading untrusted URLs without allowlist checks.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Generic WebView" --graph $GRAPH
```
