---
id: service.iam
type: service
repository: iam
status: established
evidence:
  - iam@3977c5ead95eec217fd90a158f519f5f861042b8:internal/bootstrap/apiserver/routes.go#registerUserRoutes
---

IAM owns PII / identity (auth, profile, devices, OTP). Non-PII behavioral
profile fields live in Nexus. First stop when login fails with “Failure getting
credentials” (Google login type), and for PagerDuty `iam prod` /
`k8s-iamprod` / Google Android Login / Auto Login alerts — rank IAM above
radioly for credential/login failures.
