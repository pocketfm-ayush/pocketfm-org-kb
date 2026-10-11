# Survey and CSAT

Aliases: InAppSurvey, PFMCSAT, ticket CSAT

Product context: `ios-client/pfm-kb/modules/survey-and-csat.md`

## What it is
In-app surveys and customer-satisfaction (CSAT) ticket flows.

## Graph anchors
| `InAppSurvey` | `Pocket FM/Presentation/Features/InAppSurvey` |
| `PFMCSAT` | `Pocket FM/Presentation/Features/PFMCSAT` |
| `ticketCSAT route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |

## Risks
- Prompting surveys every session — eligibility is gated.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Survey and CSAT" --graph $GRAPH
```
