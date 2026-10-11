---
id: service.ads
type: service
repository: ads
status: uncertain
evidence:
  - airflow@984e6887842e9cf1fe0966626941ff685ac40e12:temporal/ads/worker.py#main
---

Ads domain currently ships as Airflow `ads/` jobs + `temporal/ads` worker (no
standalone Pocket-Fm/ads GitHub). Deploy overlays `fm-ads` / `fm-ads-nc`.
First stop for PagerDuty `[PROD][FM-ADS]` / `FM-Ads` / `prod-fm-ads-nc` TG High
Latency and CS “ads are not loading” (pair apollo for client SDK) — not IAM.
