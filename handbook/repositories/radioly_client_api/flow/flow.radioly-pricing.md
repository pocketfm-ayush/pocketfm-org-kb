---
id: flow.radioly-pricing
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/pricing/internal/dtos.py#EpisodePricingRequestDTO
---

**Aliases:** billing pricing, coins required, episode price

**When to use:** Episode coin pricing for a Pocket FM listener. First stop `EpisodePricingRequestDTO` in `v3/pricing/internal/dtos.py`.

**Required inputs:** screen and symptom.
