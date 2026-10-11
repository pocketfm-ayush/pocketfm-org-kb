---
id: flow.nexus-upsert-user
type: flow
repository: nexus
status: established
evidence:
  - nexus@519cf4f2aae434cc3c0edb15191520ea10c03417:nexus-server/http/iam/controller.go#CreateUser
  - nexus@519cf4f2aae434cc3c0edb15191520ea10c03417:nexus-server/repository/user.go#CreateUser
---

`POST /pvt/users` (`IAMController.CreateUser`) upserts user rows into Nexus
from IAM projections. First handler for missing Nexus user after IAM signup.
