---
name: kubernetes
description: K8s workloads, probes, resources, and Pocket FM overlay patterns.
triggers: [kubernetes, k8s, kubectl, deployment, kustomize]
intent: implement
priority: 70
---

# Kubernetes

## Do
- Follow Pocket FM onboarding: overlays under Infra_deployments_k8s; Argo apps in Infra_k8s.
- Probes, resources, PDBs for user-facing services.
- ExternalSecret only for secrets; immutable image tags.
- Validate with `kubectl kustomize` before PR.

## Do not
- Invent Helm charts under Infra_k8s/Infra for first-party apps.
- Guess ECR/IRSA/DNS — ask #infra-devops.

## Related
`database-sql`, `performance-review`, `security-review`, `docker`, `kubernetes` as applicable.
