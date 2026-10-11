# Referral

Aliases: referral codes, invite program

Product context: `android-client/pfm-kb/modules/referral.md`

## What it is
Referral program entry, code sharing/redemption, and related UI.

## Graph anchors
| `referral ui` | `aural/referral/ui` |
| `referral domain` | `aural/referral/domain` |

## Risks
- Assuming referral rewards credit locally without server confirmation.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Referral" --graph $GRAPH
```
