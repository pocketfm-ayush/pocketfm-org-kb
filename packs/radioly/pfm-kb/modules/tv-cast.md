# TV and device pair

Aliases: TV cast, App Code, pair TV, pair watch, external device

## What It Is

Sign the **same login** onto a TV or watch. Not AirPlay / Chromecast
of the player.

## Actors

Logged-in listener on the phone. TV or watch is waiting, signed out.

## Journey

1. TV / watch shows a short code and two paths: phone **Settings →
   App Code**, or the web pair page after login.
2. Code lasts a few minutes.
3. Phone submits the code.
4. TV / watch waits, then lands as that account and the code is
   spent.

## User-Visible Invariants

- Phone must already be logged in. The TV cannot invent an account.
- A spent or expired code must not sign anyone in.
- Watch uses the same pair, not a second product.

## Client Behavior

Needs network. Closing the phone sheet before submit leaves the TV
unsigned-in.

## Security / PII / Compliance

Pairing hands that login (name, email, phone if on the account) to
the other device. Treat as account transfer onto a shared screen.

## Gaps

Which TVs / watches ship this, and whether web pair is every market,
are not recorded here.
