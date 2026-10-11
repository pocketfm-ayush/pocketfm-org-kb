---
id: service.infra-k8s
type: service
repository: infra-k8s
status: established
evidence:
  - Infra_k8s@8b5b599571e5e5942b85566b2dae312086872f05:README.md
  - Infra_k8s@8b5b599571e5e5942b85566b2dae312086872f05:Root Apps/CONVENTIONS.md
---

ArgoCD Application / Root Apps repo for EKS (Infra SRE). Points at workload
overlays in Infra_deployments_k8s. Do not put first-party Helm charts under
`Infra/` for app services.
