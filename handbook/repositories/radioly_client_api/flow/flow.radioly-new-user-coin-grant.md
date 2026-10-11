---
id: flow.radioly-new-user-coin-grant
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/wallet/views.py#coin_rewards
---

**Aliases:** Germany coin reward, new user free coins, DE coin grant

**When to use:** One-time Germany coin grant for a new account. First stop `coin_rewards`. Existing account or an existing grant returns a success-shaped already-registered message and does not credit again. Not daily check-in and not partner-install coins. Amount stays in server constants.

**Required inputs:** login, locale, and whether coins landed or the already-registered message showed.
