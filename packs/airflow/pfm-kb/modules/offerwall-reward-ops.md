# Offerwall Reward Ops

Aliases: tapjoy failed reward, digital turbine failed reward, ow coins earned

## What It Is
Offerwall earned-coin notifications and failed-reward recovery for Tapjoy/DT/Adjoe-style partners.

## Actors
Ops/oncall and domain owners. Listeners are affected indirectly (freshness,
entitlements, CRM, pushes) — these jobs are not usually a dedicated app screen.

## Journey
1. Schedule fires (Airflow DAG and/or Temporal schedule).
2. Job reads/writes stores or calls internal APIs.
3. Product surfaces or CRM/attribution systems see updated truth.
4. Failures typically alert Slack; users may see staleness or delayed side effects.

## User-Visible Invariants
- Lag rarely hard-crashes the app; it shows up as stale rails, late coins/unlocks,
  missing pushes, or wrong CRM/attribution state.
- DAG vs Temporal coexistence: editing the wrong runtime changes nothing live.

## Gaps
- Live cron expressions, experiment %, and coin amounts are not packed here.
- Confirm runtime ownership in source (`dags/` vs `temporal/<domain>/schedules.py`).
