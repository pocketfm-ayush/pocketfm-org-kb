---
id: flow.iam-update-profile
type: flow
repository: iam
status: established
evidence:
  - iam@3977c5ead95eec217fd90a158f519f5f861042b8:internal/bootstrap/apiserver/routes.go#registerUserRoutes
  - iam@3977c5ead95eec217fd90a158f519f5f861042b8:internal/app/user/controller.go#UpdateProfile
  - iam@3977c5ead95eec217fd90a158f519f5f861042b8:internal/app/user/service.go#UpdateProfileService
---

`PUT /v1/profile` → `UserController.UpdateProfile` → `UpdateProfileService`.
Radioly clients call this via `IAMClient.update_profile`. Related to
user.update flows that sync gender/language/fullname into IAM.
