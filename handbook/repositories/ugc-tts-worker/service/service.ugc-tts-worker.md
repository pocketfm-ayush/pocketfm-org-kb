---
id: service.ugc-tts-worker
type: service
repository: ugc-tts-worker
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/genai-tts-ugc/qa/ugc-tts-audio-generation-worker/deployment-temporal-worker.yaml
  - Infra_k8s@8b5b599571e5e5942b85566b2dae312086872f05:Root Apps/Dev/Superapps/Superapps_manifests/ugc-tts-audio-generation-worker-qa.yaml
---

UGC TTS audio-generation Temporal worker (ECR `genai-tts-temporal`, overlay
`genai-tts-ugc/.../ugc-tts-audio-generation-worker`). Catalog id
`ugc-tts-worker` matches product naming; app GitHub not accessible — deploy
overlays + Argo apps are verified SoT.
