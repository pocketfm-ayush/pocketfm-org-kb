# Device Security

Aliases: aural security, root/security module

Product context: `android-client/pfm-kb/modules/device-security.md`

## What it is
Client security checks and related protections (aural security + root security module) that can gate sensitive experiences.

## Graph anchors
| `aural security` | `aural/security/` |
| `security module` | `security/` |

## Risks
- Disabling security gates locally and shipping that to production builds.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Device Security" --graph $GRAPH
```
