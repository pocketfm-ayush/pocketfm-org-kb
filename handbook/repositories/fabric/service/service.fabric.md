---
id: service.fabric
type: service
repository: fabric
status: established
evidence:
  - fabric@56264ee2c9fc7d8141e98cf5a3ef0c9fc25178d1:playtime/cmd/main.go#main
  - fabric@56264ee2c9fc7d8141e98cf5a3ef0c9fc25178d1:impression/server/cmd/main.go#main
---

Fabric monorepo hosts playtime and impression Kafka consumers (and related
infra). Catalog `impression` also points here until a standalone repo exists.
