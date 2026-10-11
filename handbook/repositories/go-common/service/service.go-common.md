---
id: service.go-common
type: service
repository: go-common
status: established
evidence:
  - go-common@83899d7b86626fc1f8e703a892c1230683c9e021:gin/server.go#StartServer
  - go-common@83899d7b86626fc1f8e703a892c1230683c9e021:scylla/error_handler.go#FromCQLErr
---

Shared Go libraries for Pocket FM services (config, errs, gin, httpclient,
kafka, mysql/postgres/mongo/redis/scylla, temporal, experiment).
