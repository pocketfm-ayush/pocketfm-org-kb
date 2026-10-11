---
id: flow.ugc-retention-alerts
type: flow
repository: ugc-tts-worker
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/ugc-retention-temporal-schedule-worker/prod/kustomization.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/genai-tts-ugc/qa/ugc-tts-audio-generation-worker/deployment-temporal-worker.yaml
---

UGC-Retention / UGC TTS workflow failure PagerDuty alerts. Prod Temporal
schedule worker lives under `overlays/ugc-retention-temporal-schedule-worker`
and TTS audio generation under `genai-tts-ugc/.../ugc-tts-audio-generation-worker`.

**Owning repository is `ugc-tts-worker`** (this entity); also open `ugc-backend`.
Infra overlay paths are deploy evidence — not the product owner.
