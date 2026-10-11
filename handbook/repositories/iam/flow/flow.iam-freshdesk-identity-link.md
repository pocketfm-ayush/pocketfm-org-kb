---
id: flow.iam-freshdesk-identity-link
type: flow
repository: iam
status: established
evidence:
  - iam@3977c5ead95eec217fd90a158f519f5f861042b8:internal/app/callback/service.go#FreshdeskWebhook
---

Freshdesk → IAM private webhook (`/v1/webhook/freshdesk`) resolves contact /
`cf_uid` to Pocket FM UID and publishes `comms-freshdesk-events` (FM vs UGC
event names by Freshdesk group).

**When to use:** ticket “user not found”, identity linking, webhook failures —
not payment / unlock / ads product bugs. Product VOC still routes via
`flow.cs-freshdesk-triage` → radioly/ads/ugc.

**Required inputs:** Freshdesk ticket id or group; email or cf_uid when debugging
misses (`freshdesk-user-not-found` metrics).
