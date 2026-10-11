# Temporal domain workers

Aliases: temporal workers airflow repo

## What It Is
Durable domain workers that replace or shadow classic Airflow DAGs. One task
queue per domain; Slack on failure via common notify helpers.

## Domain twins
- [temporal-content-worker](temporal-content-worker.md)
- [temporal-ads-worker](temporal-ads-worker.md)
- [temporal-payments-worker](temporal-payments-worker.md)
- [temporal-experience-worker](temporal-experience-worker.md)
- [temporal-genai-worker](temporal-genai-worker.md)
- [temporal-platforms-worker](temporal-platforms-worker.md)

## Gaps
- Per-domain schedule ownership emails are infra contacts, not product PRDs.
