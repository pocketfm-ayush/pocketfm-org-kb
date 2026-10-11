# Listening progress

Aliases: playtime, resume, last listened, continue listening

## What It Is

Where they left off in a title, and the last title they played. Not
Library (saved list) and not Home.

## Actors

The logged-in listener. If a non-primary profile is chosen, progress is
that profile’s — same identity rule as Library.

## Journey

1. App asks for progress on a title (or “last story”).
2. Player / continue uses that position.
3. Web can still show an episode they only opened (zero play).

## User-Visible Invariants

- You cannot read someone else’s progress by sending their id.
- Guest / missing login falls back to the device, not another account.
- Empty progress is a miss, not a catalog error.

## Client Behavior

Needs network. Survives on the account (or profile), not only on the
device.

## Gaps

- Whether device-only last-played becomes the login’s after they sign in.
