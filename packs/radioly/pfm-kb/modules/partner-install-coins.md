# Partner-install coins

Aliases: partnership coins, CPI coins, partner redeem

## What It Is

A **one-time coin grant** after a partner install or promo
redeem (device starts it; login collects it). Not Reward Club.
Not Germany new-user coins. Not offerwall. Not ops re-engage.

## Actors

Listener on that device, then on a login. Server owns the
campaign and the amount.

## Journey

1. Device records a redeem for a live campaign.
2. After login, coins may credit once.
3. Success can show a congratulations slider (coins added).
4. Already credited on this **login** or this **device**,
   campaign off, or (for some campaigns) already a spender →
   no second credit.

## User-Visible Invariants

- One credit per login and per device for that campaign.
- Do not invent which partner or coin amount is live.
- This is not a Reward Club tier bonus on a pack.

## Client Behavior

Needs network. Closing the slider does not remove a real
credit.

## Security / PII / Compliance

Device and login are used to stop a second credit. Do not
invent retention.

## Gaps

Which partner campaigns are live, and the coin amounts, are
not recorded here.
