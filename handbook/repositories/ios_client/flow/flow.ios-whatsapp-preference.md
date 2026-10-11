---
id: flow.ios-whatsapp-preference
type: flow
repository: ios_client
status: established
evidence:
  - ios_client@edf2c101853a9f0cdef2706111c2072dd51b45d6:Pocket FM/Presentation/Features/PFMSpaceView/ViewModel/PFMOptionListVM.swift#updateWhatsappSelection
  - ios_client@edf2c101853a9f0cdef2706111c2072dd51b45d6:Pocket FM/Data/Model/UserProfileModel.swift#isWhatsApp
---

My Space WhatsApp notification toggle (`updateWhatsappSelection`) posts
`is_whatsapp` via profile update use case. Model field on `UserProfileModel`.
Client toggle wiring only — server write path is radioly `user.update` + IAM.
