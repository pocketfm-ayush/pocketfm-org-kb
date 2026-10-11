---
id: capability.scylla-from-cql-err
type: capability
repository: go-common
status: established
evidence:
  - go-common@83899d7b86626fc1f8e703a892c1230683c9e021:scylla/error_handler.go#FromCQLErr
---

Maps gocql timeouts to `QUERY_TIMEOUT_ERROR`. Go-side analogue of cassandra
`OperationTimedOut` for content-backend and other Go services.
