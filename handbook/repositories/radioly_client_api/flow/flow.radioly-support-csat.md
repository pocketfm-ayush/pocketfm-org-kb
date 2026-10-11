---
id: flow.radioly-support-csat
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/miscellaneous/views.py#csat_submit_view
---

**Aliases:** support CSAT, ticket satisfaction, rate support

**When to use:** After a support ticket, the listener rates happy or unhappy, with an optional short comment. First stop `csat_submit_view`. Not Help “was this helpful” and not the rate-the-app sheet.

**Required inputs:** ticket id and the rating or comment.
