# Not interested

Aliases: hide this, not interested, we won’t show this

## What It Is

The listener dismisses a **title** (show / book / novel) or a
**community post** so it should stop being offered. Not unsubscribe
from Library, and not autoplay “not this next” (autoplay-playlist).

## Actors

Listener. Guest / missing login falls back to the **device**, not
another account.

## Journey

1. They mark not interested on a title or post (or answer “no” on
   the “Are you interested in this story?” card).
2. Title card copy: “We won’t show this story anymore.”
3. A later “interested” / subscribe on that title is a different
   action (can land in Library’s interested area).

## User-Visible Invariants

- Guest hide is device-scoped. Login hide is login-scoped.
- This is not Library remove and not account delete.
- Post hides are remembered for about **28 days** in the store we
  have. Whether the community feed still honors that list is a gap
  (the old hide-on-profile-feed path was turned off).

## Client Behavior

Needs network. Do not claim Home already stripped the title unless
the rail is gone — Home visibility-filters do not list this rule.

## Security / PII / Compliance

The hide is tied to the login or the device. Do not invent
cross-account hide.

## Gaps

- Whether For You / Home rails actually drop a marked title.
- Whether community still hides a marked post.
