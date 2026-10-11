---
id: flow.android-whatsapp-preference
type: flow
repository: android_client
status: established
evidence:
  - android_client@f7e1318769a62f83901b7a4accfed287310f4621:common/src/main/java/com/radio/pocketfm/common/keys/PreferenceKeys.kt#IS_WHATSAPP
  - android_client@f7e1318769a62f83901b7a4accfed287310f4621:network/src/main/java/com/radio/pocketfm/network/service/Apis.kt#postProfileUpdate
  - android_client@f7e1318769a62f83901b7a4accfed287310f4621:network/src/main/java/com/radio/pocketfm/network/data/model/UserModel.kt#isWhatsapp
---

Android WhatsApp notification preference UI: local key `is_whatsapp`, model
field on `UserModel`, posts via `POST v2/user_api/user.update`
(`postProfileUpdate`). Client toggle wiring only — server write path for
preference storage is radioly `_store_whatsapp_preference` + IAM
`is_whatsapp` / `UpdateProfile`.
