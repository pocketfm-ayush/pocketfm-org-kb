---
id: flow.media-forge-deploy
type: flow
repository: media-forge
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/media-forge/qa/deployment-main.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/media-forge/prod/deployment-main.yaml
---

Deploy path for media-forge via kustomize overlays (`overlays/media-forge/qa`,
`overlays/media-forge/prod`). Image from ECR `media-forge`; binary
`/app/media-forge`. Use for rollout, HPA, ingress, or CDN-origin incidents when
app source is not cloneable.
