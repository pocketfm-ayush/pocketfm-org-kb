# Daily check-in rewards

Aliases: daily check-in, check-in calendar, jackpot day, daily rewards

## What It Is

A once-a-local-day check-in that pays coins and grows a day count.
Some days are jackpots. The calendar is a read; the check-in is the
credit.

For allocated listeners this **replaces** the listen streak. Enrollment
is decided at launch, not when they open the calendar.

## Actors

Logged-in listener. Server owns the schedule, the credit, and whether
this person is on check-in or streak.

## Journey

1. At launch, server chooses check-in or streak. Control stays on
   streak. A listener who already has streak history is not newly
   enrolled into check-in.
2. App loads the calendar (no coins).
3. Listener checks in once for today’s local date. Coins land in the
   coin wallet.
4. Consecutive local days grow the day count. A missed day resets to
   day one. A very long gap can wipe history and start fresh.
5. Some servings also show a “what you get if you come back after a
   miss” preview.

## User-Visible Invariants

- Day boundary is the listener’s local calendar day, not UTC.
- Already checked in today fails unless the app asks for current state
  (no second credit).
- Calendar must not look like a claim.
- Check-in and streak are not both tracked for the same launch.
- Do not invent daily coins, jackpot coins, or which days pay more.
  Markets use different schedules.
- Current experiments are iOS in India and US. Do not assume Android.

## Client Behavior

Needs network and login. A launch countdown can say when the next
check-in is due (next local midnight if they already claimed today).
Spam retries fail visibly. Guest / not-logged-in cannot check in.

On the rewards page, the old streak module is dropped for these
listeners.

## Product Source Of Truth

Server. The app must not invent today’s coin amount or jackpot flag.

## Gaps

Exact coins, jackpot cadence, tenure gates, and which variant is live
are not recorded here.
