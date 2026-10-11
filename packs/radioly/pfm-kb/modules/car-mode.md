# Car mode

Aliases: car mode, in-car, bluetooth car

## What It Is

A simplified in-car listen: classify the Bluetooth name, then show
a short recents row.

## Actors

Listener on a supported app vintage. **iOS is gated on.** Android
is present in source but not enabled.

## Journey

1. App sends the Bluetooth name → car / earphone / speaker / unknown
   (name-token match).
2. Intro sheet can show a few times (cap 3).
3. Recents: this login’s history, most-played first, at most four
   titles. Drop disabled, no art, or low editor score.

## User-Visible Invariants

- Earphones must not be treated as a car.
- Empty recents is allowed — do not invent popular titles.
- Library “added by me” can use this path when car mode is on.

## Client Behavior

Needs network. Recents feel warm for a few hours.

## Gaps

Whether Android will turn on, and the editor-score threshold as a
product rule vs a quality filter, are not recorded here.
