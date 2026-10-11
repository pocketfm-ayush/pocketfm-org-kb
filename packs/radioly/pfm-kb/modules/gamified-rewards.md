# Daily listen-task coins

Aliases: gamified rewards, daily challenges, claim rewards, unclaimed
rewards

## What It Is

Coins for finishing a **listen task** (unlock N episodes, sometimes
across series). Daily and weekly pots.

Some listeners are paid when the task completes. Others must
**claim**. That split is server-owned.

Not the check-in calendar. Not ops re-engage coins.

## Actors

Logged-in listener on Home, show page, or Rewards. Server owns
the task, the coins, and claim vs auto-pay.

## Journey

1. App asks if this listener is on listen-tasks.
2. Not enrolled → empty inbox, not an error.
3. Enrolled: progress on Home / show / Rewards. Finish the task.
4. Auto-pay listeners: coins land then. Claim listeners: coins
   wait in daily / weekly pots until they claim.
5. Claim updates the coin wallet.

## User-Visible Invariants

- Completing the task is not always credit. For claim listeners,
  claim is the credit.
- Daily check-in and listen-tasks are different products. Do not
  stack them as one calendar.
- Do not invent episode targets, coin amounts, or which variant
  is live.

## Client Behavior

Needs network and a login. Closing a claim sheet without claiming
leaves the pot unclaimed.

## Product Source Of Truth

Server. The app must not send “I finished, pay me” without the
server’s claim / complete step.

## Gaps

Live market/platform split, targets, and coin amounts are not
recorded here.
