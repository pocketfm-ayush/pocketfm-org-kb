# Unwind (sleep mode)

Aliases: Unwind, sleep mode, sleep stories, sleep feed

## What It Is

An evening catalog of calm stories and soundscapes. User-facing name
is **Unwind**. English only. Distinct from any older sleep-stories
partnership.

## Actors

Listener already in the Unwind test (iOS; US or India English).
CMS owns the catalog.

## Journey

1. Local evening (8pm–7am): Home can show an Unwind banner; profile
   can show Unwind; nudges / relaunch slider can fire in the same
   window.
2. Opening Unwind loads a fixed stack: premier, mood cards, popular,
   soundscapes, explore-all, quote.
3. Four mood cards: classics, relaxing, history, calm your mind.
4. Titles in this catalog are treated as free.

## User-Visible Invariants

- Hindi (and other languages) are rejected — not an empty English
  feed.
- The Unwind **feed** itself is not time-gated; Home/profile/nudges
  are.

## Client Behavior

Needs network. Demo devices can bypass the clock. Closing Unwind
returns to Home.

## Gaps

Android availability, Hindi catalog, and current day-0 enrollment
cap are not recorded here.
