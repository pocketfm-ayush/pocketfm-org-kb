# Show Referral Reward Jobs

Aliases: show referral disbursement, referee inactive reminder

Product context: `airflow/pfm-kb/modules/show-referral-rewards-jobs.md`

## What it is
Disburses show-referral rewards and reminds inactive referees.

Classic Airflow DAGs and Temporal workflows may both exist — confirm which
runtime is live before editing.

## Graph anchors
| `ShowReferralRewardWorkflow` | temporal/experience |
| Referee reminder | temporal/experience |

## Risks
- Inventing reward amounts.
- Hard-coding secrets instead of secret manager helpers.

## Query
```bash
GRAPH=airflow/graphify/graphify-out/graph.json
graphify query "Show Referral Reward Jobs" --graph $GRAPH
```
