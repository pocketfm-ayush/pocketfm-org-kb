# Auto-unlock

Aliases: auto debit, auto unlock, manage auto-unlock, continue-playing unlock

## What It Is

Per-series “keep unlocking for me” while they listen — **not**
subscription auto-renew, and not the paywall sheet.

The manage list is Continue playing, most-listened first.

## Actors

Logged-in listener on a series they already play. After a coin pay,
the server may ask them to turn this on for that series.

## Journey

1. Listener turns it on for a series (player, show page, or manage).
2. Next locked episodes spend coins without a fresh tap.
3. Manage shows Continue playing titles and each series’ on/off.
4. Not eligible, or no login, returns an empty list — not an error.

## User-Visible Invariants

- This is not “my subscription will renew.”
- On/off is account-wide for that series, not per profile. Continue
  playing on a secondary profile can still show the account toggle.
- This experience does not flip the toggle off each day.
- Some titles (audiobook path) stay on even if the listener turned
  it off.
- After a successful coin pay, a prompt to enable is not the unlock-
  confirmation sheet (that is paywall).

## Client Behavior

Needs network. Empty manage list is a valid “none / not in this
experience” state.
