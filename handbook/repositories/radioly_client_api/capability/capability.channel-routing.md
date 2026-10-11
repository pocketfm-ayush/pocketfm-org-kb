---
id: capability.channel-routing
type: capability
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/experience/account_recovery/freshdesk_helper.py#FreshdeskTicketService
---

Slack channel → first-stop owner (before multi-repo code search). Not a
substitute for alert title / VOC — use with those signals.

| Channel (name) | First stop | Notes |
|---|---|---|
| `#tech-cs-issues` / `#pocket-toons-cs` | radioly (+ Freshdesk VOC) | UID-only → expand ticket body first |
| `#going_live` | radioly | Deploy / feed TG / Credit Space PRs |
| `#sentry_content` / `#pod-content` / `#content-internal-discussions` | content-backend | Scylla / ServerError / temporal HPA |
| `#tts-ugc-prod-alerts` / `#ugc-prod-alerts-critical` | ugc-backend + ugc-tts-worker | PD titles UGC-Growth / Retention / TTS |
| Ads / FM-ADS alert channels | ads (+ apollo SDK) | Not IAM/radioly first |

**Required inputs:** channel name or permalink; for CS channels also VOC /
Freshdesk body. Do not spray onboarded repos when channel is unknown and ask
is thin.
