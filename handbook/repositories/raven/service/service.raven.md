---
id: service.raven
type: service
repository: raven
status: established
evidence:
  - raven@967f9bd0ab9d79f1f26932943292fda40177a525:cmd/main.go#main
  - raven@967f9bd0ab9d79f1f26932943292fda40177a525:internal/bootstrap/apiserver/routes.go#registerHTTPRoutes
---

Raven communications service (email/SMS/WhatsApp/push webhooks and send
providers). `cmd/main.go#main` + HTTP route registration.
