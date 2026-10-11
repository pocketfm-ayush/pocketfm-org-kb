---
id: flow.radioly-support-ticket
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/user_api/views.py#create_issue_ticket_view
---

**Aliases:** support ticket, contact support, support chat, raise a ticket

**When to use:** In-app chat that opens a support ticket. First stop `create_issue_ticket_view`. Name is required, plus phone or email. Not Help articles and not forgot-account recovery.

**Required inputs:** name and the phone or email used on the form.
