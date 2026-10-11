# Scheduled jobs

Aliases: airflow dags, backend cron jobs, temporal schedules

## What It Is
Batch and durable jobs that keep rankings, monetization ops, recon, CRM, GenAI,
and platform plumbing healthy. Classic Airflow DAGs (`dags/`) and Temporal
domain workers (`temporal/<domain>/`) coexist — confirm which is live.

## Actors
Ops/oncall. Domain owning teams. Listeners (indirect).

## Journey
Schedule fires → job updates stores/caches/CRM → product APIs or marketing see fresher data.

## Gaps
- Full DAG↔Temporal migration map is not a single doc — verify both trees.
- See domain twins under this pack’s index for product slices.
