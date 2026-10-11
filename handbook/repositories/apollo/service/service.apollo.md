---
id: service.apollo
type: service
repository: apollo
status: established
evidence:
  - apollo@14cd551ba8f280d7d0bdecc735f44ef133be3a83:service/app/service/views.py#create_media_processing_task
---

Media pipeline monorepo (Django + Celery + apollo-core). Encodes/packages
audio, video, and image assets with optional DRM. Entry API:
`POST …/media/process/` → `create_media_processing_task`.
