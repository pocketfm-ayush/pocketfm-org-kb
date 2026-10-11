# Auth and Onboarding

Aliases: login OTP email password, getting started, fill details

Product context: `android-client/pfm-kb/modules/auth-and-onboarding.md`

## What it is
Aural onboarding: login/signup (OTP, email, password), profile fill-details, and getting-started screens before home.

## Graph anchors
| `onboarding ui` | `aural/onboarding/ui` |
| `AuthConfig` | `aural/start/domain/.../AuthConfigDomainModel.kt` |

## Risks
- Inventing parallel auth JSON models instead of shared TextHelper/Cta/Media models.
- Skipping GDPR/auth-config surfaces that start already models.

## Query
```bash
GRAPH=android-client/graphify/graphify-out/graph.json
graphify query "Auth and Onboarding" --graph $GRAPH
```
