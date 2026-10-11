# Account deactivation async

## Journey
1. User requests deactivate/delete on app/API.
2. Deactivation worker processes durable teardown steps.
3. OTP/email workers may confirm.
4. User-action archives land in Cassandra/Scylla/S3.

## Modules
- [account-actions-and-deactivation](../modules/account-actions-and-deactivation.md)
- [comms-whatsapp-email-push](../modules/comms-whatsapp-email-push.md)

## Failure modes
- Partial teardown leaves PII in unexpected stores.
- Airflow hard-delete batch not aligned with this worker.
