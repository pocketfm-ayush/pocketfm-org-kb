---
id: capability.nexus-user-get
type: capability
repository: nexus
status: established
evidence:
  - nexus@519cf4f2aae434cc3c0edb15191520ea10c03417:nexus-server/repository/user.go#Get
  - nexus@519cf4f2aae434cc3c0edb15191520ea10c03417:goclient/profile_query.go#Query
---

Primary read path for Nexus user profile fields. Go client `Query` allowlists
fields including spending segments. Radioly `NexusClientService` /
`fetch_user_fields` call into this surface.
