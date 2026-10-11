---
id: capability.scylla-session-execute
type: capability
repository: python-common
status: established
evidence:
  - python-common@64749c002b42ec1255b24c1c8e268632249a5f9e:scylla/pfm_scylla/session.py#execute
---

`ScyllaSession.execute` wraps cassandra driver session.execute. Prefer this
pointer for Python `Session.execute` / timeout gold asks.
