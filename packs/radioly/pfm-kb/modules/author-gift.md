# Author gift

Aliases: gift coins, send gift, gift to author

## What It Is

The listener spends **their** coins on an author for a chapter.
Not unlock. Not a transfer to another listener wallet.

## Actors

Logged-in listener. Author is the recipient. Support can claw
back a false coin credit elsewhere.

## Journey

1. App asks for gift options. Server returns the author’s profile,
   the listener’s coin balance, and a fixed list of gift tiers.
2. Listener picks a tier and sends.
3. Success shows a thank-you. Not enough coins fails visibly
   (“add coins”).

## User-Visible Invariants

- Gift options and coin costs are server-listed. Do not invent a
  tier or a price.
- You cannot gift another account’s coins.
- A gift does not open episodes.

## Client Behavior

Needs network and a login. Closing the picker without sending
leaves the balance unchanged.

## Gaps

Whether the author actually receives spendable coins (vs a
thanks-only debit) is not proven here.
