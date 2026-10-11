# Onboarding show pick

Aliases: onboarding, first shows, pick shows, trailer grid, show selection screen

## What It Is

The first-run screens where a new listener picks starter titles (sometimes
as trailers). This is **not** AI/PGC pair routing.

## Actors

New listener. A valid show deep link or a prior pick hides the screen.

## Journey

1. Launch / onboarding config asks whether to show the pick screen.
2. Hidden if they already picked, or arrived on a real show link.
3. App loads the onboarding show rail and records the picks.

## User-Visible Invariants

- “Show selection” in Slack often means AI/PGC. Ask which one.
- Deep-linked new users should land in the show, not this picker.

## Client Behavior

Needs network. Picks persist on the account so the screen does not return
every launch.
