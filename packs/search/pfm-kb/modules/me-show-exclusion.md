# Mutual exclusion

Aliases: ME exclusion, mutual exclusion, suppressed show, device exclusion

## What It Is

A device can be barred from a group of shows. Those titles stay out of
search for that device.

## User-Visible Invariants

- Suppression is per device, not “the show is deleted.”
- Must still apply after AI/PGC or campaign logic changes which ID is in
  the list.

## Client Behavior

Server-side. Stale device state can briefly show or hide the wrong title.
