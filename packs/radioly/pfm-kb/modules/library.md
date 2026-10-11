# Library

Aliases: library, my shows, subscribed shows, my list

## What It Is

The listener’s saved / subscribed titles, not the Home catalog.
Downloads is a different Library tab (downloads), not this list.

## Actors

The logged-in listener. Identity comes from the login, not from a user id
the app stuffed in the query.

## Journey

1. App opens Library.
2. Server loads that login’s list (and profile, if a non-primary profile
   was chosen).
3. Same one-of-pair AI/PGC rule as Home.
4. If the campaign tag says Bengali or Tamil but the app sent Hindi, the
   list follows the tag.

## User-Visible Invariants

- You cannot open someone else’s library by sending their id.
- Guest / missing login falls back to the device, not another account.
- A pair still appears as one title.

## Security / PII / Compliance

Library is account-scoped. Treat a client-supplied “other user id” as
hostile.

## Client Behavior

Needs network and a login for a real list. Survives on the account, not
only on the device.
