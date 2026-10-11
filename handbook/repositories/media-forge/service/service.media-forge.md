---
id: service.media-forge
type: service
repository: media-forge
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/media-forge/qa/deployment-main.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/media-forge/qa/kustomization.yaml
  - Infra_k8s@8b5b599571e5e5942b85566b2dae312086872f05:Root Apps/Dev/Superapps/Superapps_manifests/media-forge-qa.yaml
---

Dynamic image / CDN-origin service (ECR `media-forge`, binary `/app/media-forge`).
App GitHub `Pocket-Fm/media-forge` is inaccessible to the current token; deploy
overlays + Argo app are the verified SoT until the source repo is readable.
