---
id: capability.kustomize-bases
type: capability
repository: infra-deployments-k8s
status: established
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:base/api-app/aws/v2/prod/kustomization.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:README.md
---

Shared kustomize bases (e.g. `base/api-app/aws/v2/{prod,qa}`). Overlays are
JSON-6902 patches only — do not invent first-party charts under Infra_k8s/Infra.
