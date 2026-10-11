# Coins and coin wallet

Aliases: coins, coin wallet, coin store, threshold coins, author gift

## What It Is

The listener’s **coin** balance: what they bought or were granted, what
they spent to unlock, and how many coins this lock costs. Separate from
the reward / cashback wallet (real money).

Paywall is still the sheet. This is the balance and the coin price.

## Actors

Logged-in listener. Support can claw back a false credit. Authors can
receive a coin gift.

## Journey

1. App opens wallet or hits a lock.
2. Server returns coin balance, reward balance (if any), and — on a
   lock — how many coins this title needs for this listener.
3. Spend unlocks episodes. Gift spends coins on an author.
4. Not enough coins fails visibly (“add coins”), it does not play.

## User-Visible Invariants

- You cannot read or spend another account’s coins.
- Coin price on the lock must match the show page for that listener.
  Do not invent a price or a plan id.
- Some listeners see no coin lock (free-app path). That is not the
  default.
- Follow-for-coins is gone. Do not rebuild it.

## Client Behavior

Needs network and a matching login. Purchase and spend history live on
the account. Closing the sheet without paying leaves the episode locked.

## Gaps

Checkout, playtime credits, and the Germany new-user grant are
separate modules. Live pack prices are not recorded here.
