# Account Actions and Deactivation

Aliases: user account deactivation, user_actions cassandra/s3, delete account OTP email

Product context: `kafka-stream-clients/pfm-kb/modules/account-actions-and-deactivation.md`

## What it is
Account lifecycle workers: deactivation processing, user-action dumps to Cassandra/Scylla/S3, and delete-account OTP email sends.

## Graph anchors
| `user_account_deactivation_worker_v2` | `workers/user_account_deactivation_worker_v2.py` |
| `user_actions` | `workers/user_actions/` |
| `delete_account_otp` | `workers/emails/delete_account_otp.py` |

## Risks
- Running destructive deactivation without confirming producer auth.
- Confusing with Airflow account-lifecycle batch jobs.

## Query
```bash
GRAPH=kafka-stream-clients/graphify/graphify-out/graph.json
graphify query "Account Actions and Deactivation" --graph $GRAPH
```
