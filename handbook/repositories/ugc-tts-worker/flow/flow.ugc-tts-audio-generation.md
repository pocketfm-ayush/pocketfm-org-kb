---
id: flow.ugc-tts-audio-generation
type: flow
repository: ugc-tts-worker
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/genai-tts-ugc/qa/ugc-tts-audio-generation-worker/deployment-temporal-worker.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/genai-tts-ugc/qa/ugc-tts-audio-generation-worker/scaled-object-temporal-worker.yaml
---

Temporal worker path for UGC TTS audio generation (namespace hints
`ugc-tts-qa` / `ugc-tts-prod` in scaled objects). Sibling workers under
`overlays/genai-tts-ugc/` (mastering, tier1) share the same GenAI TTS fleet.
