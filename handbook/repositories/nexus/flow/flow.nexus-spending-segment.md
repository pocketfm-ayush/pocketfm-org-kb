---
id: flow.nexus-spending-segment
type: flow
repository: nexus
status: established
evidence:
  - nexus@519cf4f2aae434cc3c0edb15191520ea10c03417:nexus-server/repository/user.go#Get
  - nexus@519cf4f2aae434cc3c0edb15191520ea10c03417:nexus-server/repository/user.go#PatchUser
  - nexus@519cf4f2aae434cc3c0edb15191520ea10c03417:nexus-server/consumer/recon/recon.go#UpdateUserReconCtrl
---

`current_spending_segment` / `lifetime_spending_segment` live on the Nexus
user document (`UserRepository.Get` / `PatchUser`), updated by recon/payment
consumers. Open here for spender-segment bugs — not IAM.
