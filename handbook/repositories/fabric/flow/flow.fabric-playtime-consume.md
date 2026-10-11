---
id: flow.fabric-playtime-consume
type: flow
repository: fabric
status: established
evidence:
  - fabric@56264ee2c9fc7d8141e98cf5a3ef0c9fc25178d1:playtime/audioplaytime/service.go#ProcessEvent
  - fabric@56264ee2c9fc7d8141e98cf5a3ef0c9fc25178d1:playtime/cmd/main.go#main
---

Audio playtime consumer `ProcessEvent` under `fabric/playtime`. Complements
kafka-stream-clients playtime writers; confirm which surface owns a given
playtime topic before changing both.
