---
id: flow.content-temporal-hpa
type: flow
repository: content-backend
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/content-temporal-schedule-worker/prod/deployment-temporal-worker.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/content-temporal-schedule-worker/prod/scaled-object-temporal-worker.yaml
---

`content-temporal-schedule-worker-prod` KubeHpaMaxedOut / KEDA HPA maxed alerts.
Content Temporal schedule worker overlays under
`overlays/content-temporal-schedule-worker`. Pair with content-backend POD
memory/latency spikes; infra-deployments-k8s owns the HPA/scaled-object patch.
