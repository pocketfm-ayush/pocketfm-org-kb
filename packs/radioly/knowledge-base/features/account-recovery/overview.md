# Account recovery

Aliases: forgot account, raise issue, find my account

Product context: `radioly/pfm-kb/modules/account-recovery.md` · flow `radioly/pfm-kb/flows/recover-account.md`

## What it is

Login support form. Success is “we received your issue,” not a login
or merge. Account-transfer is the internal merge.

## Graph anchors

| Symbol | Source |
|---|---|
| account recovery | `v3/experience/account_recovery/` |


## Key product notes

The login path for a listener who cannot find their account. They file
a support request; they do **not** get an instant login. Distinct from
account-transfer (internal merge of two known ids).

## Risks

- Treating success as “you are logged in.”
- Opening a second ticket from the same device the same day.

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "account recovery" --graph $GRAPH
```
