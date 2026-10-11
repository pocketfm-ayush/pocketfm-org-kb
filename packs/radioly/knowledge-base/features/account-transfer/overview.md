# Account transfer

Aliases: account merge, move account, old account to new account

Product context: `radioly/pfm-kb/modules/account-transfer.md`

## What it is

Internal merge of listening and unlocks. Not the login “Forgot account?”
form (`account-recovery`). Not a consumer settings screen.

## Graph anchors

| Symbol | Source |
|---|---|
| account transfer | `v3/experience/account_transfer/` |


## Key product notes

An **internal** merge: listening and unlocks on one account are moved
onto another. This is **not** the login “Forgot account?” form (that is
account-recovery) and **not** a listener settings screen.

## Risks

- Treating a client-supplied “move their id to mine” as a consumer feature.
- Confusing this with account-recovery success (which is not a login).

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "account transfer" --graph $GRAPH
```
