---
id: flow.client-attribution-event
type: flow
repository: go-radioly
status: established
evidence:
  - go-radioly-service@ea177db5c63c685e0f91a322e8ada290cf37f999:internal/gateway/eventlog/controller.go#LogEvents
---

Client attribution / eventlog ingest via `LogEvents` on the gateway eventlog
controller. First stop for client→server event logging bugs owned by go-radioly.
