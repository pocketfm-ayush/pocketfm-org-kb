---
id: flow.ads-fm-ads-latency
type: flow
repository: ads
status: uncertain
evidence:
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/fm-ads-nc/prod/deployment-main.yaml
  - Infra_deployments_k8s@41f9932ae426e892c2e259322671d63e4fa60034:overlays/fm-ads/prod/deployment-main.yaml
  - airflow@984e6887842e9cf1fe0966626941ff685ac40e12:temporal/ads/worker.py#main
---

PagerDuty `[PROD][FM-ADS]` / `FM-Ads` / `prod-fm-ads-nc` TG High Latency P99 and
CS “ads are not loading”.

**Owning repository is `ads`** (this entity). Pair `apollo` for client SDK.
Airflow `temporal/ads` and Infra overlays `fm-ads` / `fm-ads-nc` are deploy /
async evidence only — not the catalog owner. Open ads (+ apollo) before IAM
or radioly.
