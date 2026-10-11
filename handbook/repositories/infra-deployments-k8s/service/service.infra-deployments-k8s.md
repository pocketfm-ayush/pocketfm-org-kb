---
id: service.infra-deployments-k8s
type: service
repository: infra-deployments-k8s
status: established
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:docs/SERVICE_ONBOARDING.md
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:README.md
---

Workload kustomize manifests for Pocket FM services
(`overlays/<service>/<env>/` on shared `base/`). ArgoCD Application objects
live in Infra_k8s, not here. Docs-safe SoT for service onboarding layout.
