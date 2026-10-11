# Account delete

Aliases: delete account, close account, account deletion

Product context: `radioly/pfm-kb/modules/account-delete.md` · flow `radioly/pfm-kb/flows/close-account.md`

## What it is

User-initiated account deletion. Distinct from deactivate / recovery.

## Graph anchors

Search CODE SEARCH for `delete_account` / account deletion views under `v2/user_api/` and `v3/`.
Confirm handlers before naming them in answers.


## Key product notes

The listener asks to **remove** this login. Distinct from deactivate
(pause), account-recovery (lost login ticket), and account-transfer
(internal merge).

## Risks

- Confusing delete with deactivate or transfer.
- Claiming data retention policy without a packed source.

## Related
- `account-deactivate`
- `ugc-backend-writer`
- `iam-identity`

## Query
```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "account delete" --graph $GRAPH
```
