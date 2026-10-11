---
id: flow.ugc-backend-deploy
type: flow
repository: ugc-backend
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/ugc-backend/qa/main/deployment-main.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/ugc-backend/prod/deployment-main.yaml
---

Deploy path for ugc-backend main workload via kustomize overlays (qa/main,
prod). Image tags come from ECR `ugc-backend/<env>`. Use for UGC-GROWTH
latency / Moderation Pending production incidents routed to ugc-backend TG.
Source handlers unknown until `Pocket-Fm/ugc-backend` is cloneable.
