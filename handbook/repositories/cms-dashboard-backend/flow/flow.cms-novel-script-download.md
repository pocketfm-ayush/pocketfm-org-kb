---
id: flow.cms-novel-script-download
type: flow
repository: cms-dashboard-backend
status: established
evidence:
  - cms-dashboard-backend@97dae77fe95ee18e2db75e93166b3f94e7e6a390:v2/content_api/views.py#get_active_scripts
---

CMS novel/show script download on `cms.pocketfm.com` (“cannot download the
script of this novel”). `get_active_scripts` is the active-scripts API — first
stop in `#bug-discussions-cms` before radioly or novels airflow.
