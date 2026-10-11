---
id: flow.media-process-create
type: flow
repository: apollo
status: established
evidence:
  - apollo@14cd551ba8f280d7d0bdecc735f44ef133be3a83:service/app/service/views.py#create_media_processing_task
---

`create_media_processing_task` (routed at `media/process/`) creates a media
processing job and kicks the Celery/Temporal pipeline.
