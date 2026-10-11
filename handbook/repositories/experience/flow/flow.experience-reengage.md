---
id: flow.experience-reengage
type: flow
repository: experience
status: uncertain
evidence:
  - airflow@984e6887842e9cf1fe0966626941ff685ac40e12:temporal/experience/worker.py#main
  - kafka-stream-clients@84a90c1797a9b6711c25e142c7f4b604f8b49c1c:workers/experience/user_reengage_reward_worker.py#KafkaConsumerProcess
---

Reengage rewards and related experience loops: Temporal worker in airflow plus
kafka `KafkaConsumerProcess` under `workers/experience/`.
