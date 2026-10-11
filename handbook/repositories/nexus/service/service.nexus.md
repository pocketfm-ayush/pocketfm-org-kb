---
id: service.nexus
type: service
repository: nexus
status: established
evidence:
  - nexus@519cf4f2aae434cc3c0edb15191520ea10c03417:nexus-server/bootstrap/apiserver/routes.go#registerAppRoutes
  - nexus@519cf4f2aae434cc3c0edb15191520ea10c03417:nexus-server/repository/user.go#Get
---

Nexus stores non-PII user/device behavioral profile (spending segments,
subscription/biz-model flags). Synced from IAM create-user/device events and
payment/recon consumers. Do not put PII here — that is IAM.
