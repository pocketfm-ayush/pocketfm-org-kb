---
id: flow.content-fm-server-error
type: flow
repository: content-backend
status: established
evidence:
  - content-backend@9dfd1a187c6da0b9ee1dcaac4ea61b1917c5262b:internal/bootstrap/apiserver/errorhandler.go#HandleHTTPError
  - content-backend@9dfd1a187c6da0b9ee1dcaac4ea61b1917c5262b:internal/redis/redis_manager.go#InitConnections
  - content-backend@9dfd1a187c6da0b9ee1dcaac4ea61b1917c5262b:internal/mysql/mysql_manager.go#InitConnection
---

content-fm ServerError / network / connection failures. Gin maps domain errors
via `HandleHTTPError` / `HandleError`; Redis cluster connect failures and MySQL
connect failures raise `InternalServerError`. On-call for content-fm ServerError
or datastore client path issues: inspect `content-backend` first (not radioly).
Scylla timeouts stay on `capability.scylla-cql-query` / `QueryString`.
