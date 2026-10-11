---
id: flow.cs-freshdesk-triage
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/experience/account_recovery/freshdesk_helper.py#FreshdeskTicketService
---

CS Slack pings that only paste `pocketfm.freshdesk.com/a/tickets/<id>` + UID
(no VOC / subject / description) are **not** code-locate asks.

Required inputs before ownership locate:
1. Freshdesk **subject + description** (VOC), or set `FRESHDESK_API_KEY` so
   Groot expands the ticket.
2. Symptom words (coins, unlock, ads, login, progress, …) — not UID alone.
3. Alert / service name when it is a PagerDuty thread.

Do **not** multi-repo code-search while the ticket body is missing. After expand,
route by symptom: payments/unlock → radioly; ads loading → ads (+ apollo);
Google login credentials → iam; UGC retention/TTS alerts → ugc-tts-worker.
