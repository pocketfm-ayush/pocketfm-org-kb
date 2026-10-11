---
id: flow.radioly-playtime-credits
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/services/mhp/services/playtime_credits.py#PlaytimeCreditsService
---

**Aliases:** Unlock+, hours pass, playtime credits, time wallet

**When to use:** Hours or minutes that unlock episodes. First stop `PlaytimeCreditsService`. Not the coin balance and not the resume position on a show.

**Required inputs:** login and whether the ledger shows hours or a coin spend.
