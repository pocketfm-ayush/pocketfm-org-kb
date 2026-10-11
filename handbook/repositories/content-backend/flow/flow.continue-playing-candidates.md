---
id: flow.continue-playing-candidates
type: flow
repository: content-backend
status: established
evidence:
  - content-backend@9dfd1a187c6da0b9ee1dcaac4ea61b1917c5262b:internal/app/continueplaying/controller.go#GetCandidates
---

`GetCandidates` ranks continue-playing show candidates from Valkey/Scylla.
Home CP module assembly remains radioly-side.
