---
id: flow.radioly-logged-out-purchase
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/logged_out_transaction/banner_service.py#inject_paywall_banner
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/logged_out_transaction/banner_service.py#inject_mystore_banner
---

**Aliases:** guest checkout continuity, offers refreshed banner, pack not
available.

**When to use:** After a logged-out coin checkout, paywall or My Store shows
a one-time notice that the pack was bought, is unavailable, or offers
refreshed. Information only — no deeplink. Paywall and My Store only. A
stale or future timestamp shows nothing. Banner failure must not break the
sheet.

**Required inputs:** whether checkout started logged out, the screen, and
how long ago the attempt was.
