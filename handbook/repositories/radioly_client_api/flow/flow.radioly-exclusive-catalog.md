---
id: flow.radioly-exclusive-catalog
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/subs_exclusive_catalog/service_manager.py#SubsExclusiveCatalogManager
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/subs_exclusive_catalog/services/show_service.py#SECShowService
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v3/payments/subs_exclusive_catalog/services/plan_service.py#SECPlanService
---

**Aliases:** subs exclusive, subscribe to unlock series, SEC.

**When to use:** A show locks after a short free sample with subscribe copy,
or a subscriber still sees locks on an exclusive title. Membership is the
hardcoded show list in this package, applied on show details, paywall, ads,
and unlocking. Home and search do not hide these shows. Subscriber awareness
is once per show. Not a Pocket Novel catalog.

**Required inputs:** show id, UID, and whether the listener is subscribed.
