---
id: service.content-backend
type: service
repository: content-backend
status: established
evidence:
  - content-backend@9dfd1a187c6da0b9ee1dcaac4ea61b1917c5262b:internal/bootstrap/apiserver/routes.go#registerInternalRoutes
  - content-backend@9dfd1a187c6da0b9ee1dcaac4ea61b1917c5262b:internal/repository/query.go#QueryString
---

Go Gin catalog platform (MySQL + optional Scylla + Valkey/Redis). Private
`/internal/show*` / stories / continue-playing APIs for Radioly and other BFFs.
First stop for content-fm ServerError / network connection failures
(`HandleHTTPError`, Redis/MySQL `InternalServerError`), Scylla
OperationTimedOut (`QueryString`), content-backend POD memory spikes /
latency, and `content-temporal-schedule-worker-prod` KubeHpaMaxedOut alerts.
