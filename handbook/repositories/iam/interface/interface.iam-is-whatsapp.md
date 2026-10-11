---
id: interface.iam-is-whatsapp
type: interface
repository: iam
status: established
evidence:
  - iam@3977c5ead95eec217fd90a158f519f5f861042b8:internal/app/auth/dto.go#IsWhatsapp
  - iam@3977c5ead95eec217fd90a158f519f5f861042b8:internal/app/user/controller.go#UpdateProfile
---

WhatsApp notification toggle does not persist after refresh — IAM side:
`is_whatsapp` on auth DTOs and `PUT /v1/profile` (`UpdateProfile`). Paired with
radioly `user.update` / `_store_whatsapp_preference` (UsersMeta). Rank IAM +
radioly above android/ios UI for persistence bugs.
