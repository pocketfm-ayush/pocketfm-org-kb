---
id: service.ugc-backend
type: service
repository: ugc-backend
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/ugc-backend/qa/main/deployment-main.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/ugc-backend/qa/main/serviceaccount.yaml
---

UGC creator backend (ECR `ugc-backend`). Distinct from `writers-backend`
(Django UGC APIs) and `ugc-ui` (browser UI). App GitHub inaccessible to
current token; QA/prod overlays under `overlays/ugc-backend/` are verified.

**When to use** — first stop for PagerDuty `UGC-GROWTH` / `UGC-Growth` /
`UGC-Retention` / Moderation Pending / `[ugc-growth-kafka]` /
`DescGenerationService` / Gemini empty description / `tier1-job-struck`
audio-stack TTS jobs — not radioly. Prefer `writers-backend` for documented
Django `/v2/content_api` UGC routes and partner.pocketfm.com creator signup.
Prefer `ugc-ui` for creator web UI deploy, ingress, or front-end-only incidents.
