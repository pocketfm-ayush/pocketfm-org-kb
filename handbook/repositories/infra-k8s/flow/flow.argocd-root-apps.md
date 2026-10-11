---
id: flow.argocd-root-apps
type: flow
repository: infra-k8s
status: established
evidence:
  - Infra_k8s@8b5b599571e5e5942b85566b2dae312086872f05:Root Apps/Prod/prod.yaml
  - Infra_k8s@8b5b599571e5e5942b85566b2dae312086872f05:Root Apps/CONVENTIONS.md
---

ArgoCD root Application hierarchy under `Root Apps/` (Prod/Dev/Infra).
QA apps first, then prod — cross-link PRs with Infra_deployments_k8s overlays.
