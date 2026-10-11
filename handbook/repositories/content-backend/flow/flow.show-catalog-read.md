---
id: flow.show-catalog-read
type: flow
repository: content-backend
status: established
evidence:
  - content-backend@9dfd1a187c6da0b9ee1dcaac4ea61b1917c5262b:internal/app/show/controller.go#GetShow
  - content-backend@9dfd1a187c6da0b9ee1dcaac4ea61b1917c5262b:internal/bootstrap/apiserver/routes.go#registerInternalRoutes
---

`GetShow` / show stories / batch query endpoints are authoritative show
metadata reads. Radioly remains consumer BFF for many journeys.
