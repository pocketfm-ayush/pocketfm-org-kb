---
id: service.ugc-ui
type: service
repository: ugc-ui
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/ugc-ui/qa/main/deployment-main.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/ugc-ui/qa/pre-deployment/deployment-main.yaml
---

Creator-facing UGC web UI (ECR `ugc-ui`). App GitHub inaccessible; overlays
under `overlays/ugc-ui/` (main + feature branches) are verified deploy SoT.

**When to use** — creator web UI load errors, ingress/TG deploy questions,
pre-deployment or feature-branch rollouts, and front-end-only UGC studio bugs.
Use **`ugc-backend`** for API latency, kafka growth jobs, moderation queues,
DescGeneration / TTS pipeline alerts, and backend PagerDuty titles — not this UI.
