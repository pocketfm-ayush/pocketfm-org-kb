# Streaks

Aliases: listen streak, daily streak, streak config, keep the streak

## What It Is

Launch tells the app whether to track a **listen streak** or **daily
check-in**. Those two are alternatives for one launch, not a stack.

The listen streak is a day-count the listener keeps by coming back
(listen / claim). This slice only owns that launch choice and the
countdown. Claim rules and coin amounts live with the older streak
product.

## Actors

Listener (device required). Server owns which track and the next-due
countdown.

## Journey

1. App asks for streak config at launch.
2. If daily check-in is active for this listener, the answer is
   “track check-in” plus seconds until the next check-in. No streak
   config.
3. Otherwise the answer is “track streak” plus seconds until the next
   streak due, and (when enrolled) the current count and broken-state
   art.
4. A guest or invalid login is not told to track streak.

## User-Visible Invariants

- Check-in enrollment is decided at launch, not mid-session.
- Missing more than one local day can show the streak as broken and
  hide the count.
- Do not invent streak coin amounts, reclaim prices, or which listen
  action claims the day. Those are not stable in this slice.

## Client Behavior

Needs network. The countdown is a launch signal so the app knows when
to prompt again. Opening Home does not by itself claim the day.

## Product Source Of Truth

Server launch config. The app must not decide “this user is on
check-in” locally.

## Gaps

Claim action, reward schedule, reclaim, and current streak experiment
are not recorded here.
