---
id: flow.raven-email-routes
type: flow
repository: raven
status: established
evidence:
  - raven@967f9bd0ab9d79f1f26932943292fda40177a525:internal/bootstrap/apiserver/routes.go#registerEmailRoutes
  - raven@967f9bd0ab9d79f1f26932943292fda40177a525:internal/providers/email/sendgrid/service.go#Send
---

Email send path: public `/v1` email routes plus provider `Send`
(SendGrid/SES). First stop for transactional email delivery bugs.
