# Account Actions and Deactivation

## What It Is
Async account teardown and durable user-action archives.

## Actors
Listeners deleting/deactivating; compliance; account workers.

## Security / PII / Compliance
Account and action logs are highly sensitive.

## Gaps
Airflow may own scheduled hard-delete batches — verify runtime.
