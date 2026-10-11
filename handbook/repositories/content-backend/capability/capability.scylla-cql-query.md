---
id: capability.scylla-cql-query
type: capability
repository: content-backend
status: established
evidence:
  - content-backend@9dfd1a187c6da0b9ee1dcaac4ea61b1917c5262b:internal/repository/query.go#QueryString
---

CQL reads use `session.Query` + go-common `FromCQLErr` (timeouts →
`QUERY_TIMEOUT_ERROR`), not Python `Session.execute`. Gold Scylla
OperationTimedOut / connection failures for content-fm start here.
