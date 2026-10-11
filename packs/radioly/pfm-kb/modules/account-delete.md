# Account delete

Aliases: delete account, remove account, close account

## What It Is

The listener asks to **remove** this login. Distinct from deactivate
(pause), account-recovery (lost login ticket), and account-transfer
(internal merge).

## Actors

Logged-in listener. A confirm step can require a code or a short-lived
delete token.

## Journey

1. They start delete from the app while logged in.
2. If a delete is already in progress: “in progress,” not a second
   request. If already deleted: already-deleted copy.
3. Start copy: deletion **completes in 30 days**.
4. A confirm path can also cancel an active subscription as part of
   delete.
5. Signing in again on a deleted login can **undo** the request. The
   display name may come back as a generic “PocketFM User.”

## User-Visible Invariants

- Delete is not deactivate and not “Forgot account?”
- In-progress delete rejects a second start.
- Do not treat start as “gone this second” in copy — the 30-day line
  is what the product says. What they can still play during those
  days is a gap.
- Guest / missing login cannot delete someone else’s account.

## Client Behavior

Needs network and a login. Closing the sheet without confirm does not
start delete.

## Security / PII / Compliance

**Sensitive.** Login identifiers and a delete token / confirm code.

- Do not invent retention, lawful basis, or what is erased vs kept.
- Do not log tokens or confirm codes.

## Gaps

- Whether every in-app delete cancels the pass, or only the
  token-confirm path.
- What the listener can still open during the 30 days.
- Legal meaning of the 30-day line.
