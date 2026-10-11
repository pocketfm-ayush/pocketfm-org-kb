---
id: flow.ugc-growth-alerts
type: flow
repository: ugc-backend
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/ugc-backend/prod/deployment-main.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/ugc-backend/qa/main/deployment-main.yaml
---

PagerDuty / Slack titles: `[PROD][UGC-GROWTH]`, `ugc-growth-kafka`,
`DescGenerationService`, `Moderation Pending`.

**Owning repos:** `ugc-backend` (this entity) for growth/moderation TG;
`ugc-tts-worker` + retention temporal schedule for `[PROD][UGC-RETENTION]` /
`tier1-job-struck` / TTS schedule (see `flow.ugc-retention-alerts`). Infra
overlay paths are deploy evidence only — do **not** treat
`Infra_deployments_k8s` as the product owner.
