---
id: capability.iam-user-meta-props
type: capability
repository: iam
status: established
evidence:
  - iam@3977c5ead95eec217fd90a158f519f5f861042b8:internal/app/user/service.go#UpdateUserMetaProps
  - iam@3977c5ead95eec217fd90a158f519f5f861042b8:internal/repository/user_meta.go#UpdateUserMeta
---

IAM can merge key/value pairs into user meta `props` via
`UpdateUserMetaProps`. Prefer this when investigating identity-side storage
of preference flags that land in meta props (alongside radioly UsersMeta).
