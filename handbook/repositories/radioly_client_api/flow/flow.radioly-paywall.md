---
id: flow.radioly-paywall
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/paywall_orchestrator/orchestrator_service.py#PaywallOrchestrator
---

**Aliases:** paywall, buy sheet, unlock sheet, coin sheet, subscription wall

**When to use:** The lock sheet: what the listener can buy or watch-an-ad for. Server chooses the sheet. First stop `PaywallOrchestrator`.

**Required inputs:** screen and symptom.
