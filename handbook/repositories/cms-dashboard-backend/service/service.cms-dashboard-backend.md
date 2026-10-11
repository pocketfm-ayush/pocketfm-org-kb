---
id: service.cms-dashboard-backend
type: service
repository: cms-dashboard-backend
status: established
evidence:
  - cms-dashboard-backend@97dae77fe95ee18e2db75e93166b3f94e7e6a390:v2/content_api/views.py#get_qc_details
  - cms-dashboard-backend@97dae77fe95ee18e2db75e93166b3f94e7e6a390:v2/content_api/topics/views.py#get_topic_details
---

Internal CMS Django backend for content ops (QC, topics, campaigns,
experiments, daily episode release / N7 bank scheduling). Distinct from
writers-backend and radioly. First stop for `#bug-discussions-cms` Raw QC /
voice artist / creator ID / novel script download (`get_active_scripts`) on
`cms.pocketfm.com`, `[cms-studio]` PPV errors, and “no new episodes released”
commitment breaches (pair airflow for batch jobs).
