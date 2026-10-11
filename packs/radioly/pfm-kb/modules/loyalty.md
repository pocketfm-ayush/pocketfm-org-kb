# Loyalty (Reward Club)

Aliases: Reward Club, Premium Club, loyalty tiers, Plus, Pro, Pro+

## What It Is

A logged-in club: last-year listening and coin spend become a named tier,
then extra coins on coin-pack buys. A weekly Plus (also shown as Pro)
layer can raise that bonus for a calendar week.

Germany copy uses Premium-Club. The app does not pick the ladder or the
bonus.

## Actors

Listener (must be logged in). Server owns tier, Plus, bonus, and sheet
copy. Ops can inspect or adjust a member via an internal tool.

## Journey

1. App asks for Reward Club, webview, or a surface banner.
2. Server decides if this listener is in the club (market, platform,
   tenure, experiment).
3. Daily: re-score the tier from the rolling last-year hours and coins
   spent. A listener can skip a rung, rise, or drop.
4. Weekly: if this week’s coin spend hits their Plus target, Plus is
   granted for the *next* calendar week. This week’s Plus is already
   earned or not.
5. On coin-pack screens (not subscriptions), extra coins show at the
   current bonus.
6. After a successful pack buy, the success sheet can show the bonus.

## User-Visible Invariants

- Do not invent the ladder. Some markets show five named tiers (Bronze
  through Diamond). Some India servings stop at Gold.
- A stored tier that is not on the current ladder is re-scored. Do not
  leave a ghost tier on screen.
- Falling below the first rung can lose the club. Plus on a week can
  block a drop all the way to “no tier.”
- Losing Plus does not by itself drop the annual tier.
- Bonus does not apply to subscriptions.
- If a weekly-challenge product is live for this listener, loyalty’s
  weekly Plus path is off.
- Do not invent hours, coin thresholds, bonus percent, or Plus targets.

## Client Behavior

Needs network and login. Surfaces: Home banner, show page, My Store,
bottom slider, Rewards Club page, Android webview, pay success. Closing
a banner does not change tier. Logout must not keep another person’s
club.

Android can play a loyalty intro audio ad. That is not the paywall.

## Event Meaning

Tier up/down, retention or nudge, Plus unlocked (next week) vs Plus
activated (this week). Used for sliders, pushes, and analytics — not
for inventing copy or amounts.

## Product Source Of Truth

Server. The app must not send “I am on tier X” or “I am Plus.”

## Gaps

Which experiment is live, exact hours/coins thresholds, bonus percent,
and the Plus spend-target formula are not recorded here.
