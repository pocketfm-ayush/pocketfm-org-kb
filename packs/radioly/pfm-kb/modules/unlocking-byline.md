# Unlocking byline

Aliases: unlock byline, free tomorrow label, lock message styling

## What It Is
On the show page, labels that explain *how* an episode unlocks (plan name,
“free tomorrow”, styled lock chip). Does not change how many episodes are open.

## Actors
Listener. Show-details UI. Experiment allocation for byline variants.

## Journey
1. Listener opens a show.
2. If eligible for the byline experiment, episodes get lock/unlock labels.
3. Listener understands next unlock path without entering paywall necessarily.

## User-Visible Invariants
- Byline is copy/UI — unlock count still comes from unlock state.
- Some paid plans hide byline text by design.
- Related: [show-details-and-unlock](show-details-and-unlock.md), [auto-debit](auto-debit.md).

## Gaps
- Exact strings and colours are config/locale — verify before claiming copy.
