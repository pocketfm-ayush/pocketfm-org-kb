# Close account

Participating modules: account-delete, account-deactivate,
account-recovery, account-transfer, otp-login.

## Journey

1. Logged-in settings: **deactivate** (pause days / until next login)
   or **delete** (30-day remove; confirm code or token).
2. Delete-in-progress or already-deleted → do not start a second
   delete.
3. Login after deactivate → pause ends.
4. Login after delete → request can be undone; not a new recovery
   ticket.

## User-Visible Invariants

- Recovery never deletes or merges.
- Transfer is internal; the listener has no merge button.
- Deactivate copy must not use the 30-day delete line.

## Failure modes

- Confirm token / code expired → delete does not start.
- Already deactivated → already-paused, not delete.
