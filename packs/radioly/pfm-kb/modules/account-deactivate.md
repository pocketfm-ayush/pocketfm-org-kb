# Account deactivate

Aliases: deactivate account, pause account, until login

## What It Is

The listener **pauses** this login for a while, or until they sign in
again. Not delete (30-day remove), not recovery, not transfer.

## Actors

Logged-in listener.

## Journey

1. They pick how long: a number of days, or until the next login.
2. Already paused: already-deactivated, not a second pause.
3. Signing in again **lifts** the pause.

There is no listener “undo pause” button in the current app path;
login is the undo.

## User-Visible Invariants

- Deactivate is not delete. Do not show 30-day delete copy here.
- Until-login means the next successful session ends the pause.
- A timed pause ends on that date.

## Client Behavior

Needs network and a login.

## Security / PII / Compliance

**Sensitive.** The paused login’s email / phone / name are stored with
the pause request.

- Do not invent retention or who may lift a pause besides the listener
  signing in.

## Gaps

- What Home / library / paywall look like while paused, before they
  sign in again.
- Whether a dedicated “reactivate” control exists on any vintage.
