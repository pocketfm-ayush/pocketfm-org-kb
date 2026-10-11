---
id: flow.media-forge-cdn-image
type: flow
repository: media-forge
status: uncertain
evidence:
  - apollo@14cd551ba8f280d7d0bdecc735f44ef133be3a83:core/specs/bucket_cdn_mapping.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/media-forge/qa/ingress.yaml
---

Apollo maps IMAGE bucket CDN to `media-forge-qa-cdn.pocketfm.org` (QA). Ingress
and deployment live under `overlays/media-forge/`. Use this when warming or
serving transformed images; app code path pending GitHub access.
