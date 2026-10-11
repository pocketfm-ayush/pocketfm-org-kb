# Auth and Onboarding

Aliases: PFMOnboardingView, OTP, create user

Product context: `ios-client/pfm-kb/modules/auth-and-onboarding.md`

## What it is
Login/signup, OTP verification, and first-run profile creation before full home access.

## Graph anchors
| `PFMOnboardingView` | `Pocket FM/Presentation/Features/PFMOnboardingView` |
| `otpVerification route` | `Pocket FM/Presentation/Navigation/AppRoutes.swift` |
| `PFMCreateUserView` | `Pocket FM/Presentation/Features/UserViews/PFMCreateUserView` |

## Risks
- Skipping GDPR consent gates that may block EU flows.
- Inventing auth models in Presentation instead of Data layer.

## Query
```bash
GRAPH=ios-client/graphify/graphify-out/graph.json
graphify query "Auth and Onboarding" --graph $GRAPH
```
