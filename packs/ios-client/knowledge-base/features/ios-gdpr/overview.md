# GDPR Consent

Aliases: GDPRConsent, privacy do-not-sell

Product context: `ios-client/pfm-kb/modules/gdpr-consent.md`

## What it is
Consent and privacy choice surfaces including GDPR and do-not-sell style settings routes.

## Graph anchors
| `GDPRConsent` | `Pocket FM/Presentation/Features/GDPRConsent` |
| `doNotSell route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |
| `privacyPolicy route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Shipping EU builds that skip consent gates.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "GDPR Consent" --graph $GRAPH
```
