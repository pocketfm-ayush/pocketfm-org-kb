---
id: capability.scylla-operation-timed-out
type: capability
repository: kafka-stream-clients
status: established
evidence:
  - kafka-stream-clients@84a90c1797a9b6711c25e142c7f4b604f8b49c1c:workers/experience/key_tropes/key_tropes_worker.py#KeyTropesWorker
---

Python cassandra `OperationTimedOut` is handled in kafka workers (e.g.
`KeyTropesWorker`). Pair with content-backend Go `FromCQLErr` / python-common
`ScyllaSession.execute` when on-call asks about Scylla timeouts.
