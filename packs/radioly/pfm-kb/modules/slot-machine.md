# Slot machine (Lucky Spin)

Aliases: lucky spin, spin and win, slot machine, reward spin

## What It Is

A cooldown-gated spin that can credit coins. Odds are not the same for
every listener. The server returns whether they can spin, when the next
spin is allowed, and what this spin paid.

## Actors

Listener on Home (banner or bottom slider) or the spin webview. Server
owns eligibility, outcome, and cooldown.

## Journey

1. App asks if this listener can spin.
2. If the feature is off for them, the app must not show a working
   spin.
3. On spin: server claims the attempt, picks an outcome from their
   spend cohort, credits coins if the outcome is above zero, then
   starts cooldown.
4. After a spin they cannot spin again until the server’s next-eligible
   time.

## User-Visible Invariants

- Zero coins is a possible outcome for some cohorts. Do not treat
  “spin” as “always pays.”
- A blocked spin (cooldown or a second tap) pays nothing.
- Do not invent coin amounts, odds, or cooldown hours. Eligibility
  payload owns the hours.
- Some servings give a better first-ever spin. Do not invent that
  floor.
- Home nudge is impression-capped. Do not invent the cap.

## Client Behavior

Needs network. Home can show an active vs cooldown banner (including a
countdown art). Closing the slider does not grant a spin. Wallet
history should show a fresh credit without waiting a day.

## Event Meaning

Spin executed vs spin blocked (cooldown or concurrent claim). Used for
analytics and a post-spin push — not for inventing the prize.

## Product Source Of Truth

Server. The app must not pick the reel result.

## Gaps

Live market/platform split, exact odds, first-spin floor, and cooldown
hours are not recorded here.
