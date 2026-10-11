# Trailer code

Aliases: show code, remember the code, find my show

## What It Is

A first-run prompt: “Do you remember the show code?” The listener types
a two-digit code from a trailer or ad. This is **not** the title-picker
grid (onboarding-show-pick).

## Actors

New (day-zero) iOS listener in the US, from a matching ad set.
Internal tools assign or disable a code on a show (one active code
per show).

## Journey

1. First-run can show the code prompt instead of (or with) the picker.
2. They enter a code (10–99). “FIND MY SHOW.”
3. Hit: “We found your show” / “Continue watching for free.”
4. Miss: “this code does not match” — a normal miss, not a crash.

## User-Visible Invariants

- Wrong or unknown code is expected. Do not treat it as a server outage.
- Codes are two digits. A show has at most one active code.
- “Free episodes available” is server copy; do not invent how many or
  how that interacts with the paywall.

## Client Behavior

Needs network. Search needs a login. Eligibility is first-day iOS US;
reinstalls and older devices do not get this prompt.

## Gaps

- Where the listener first sees the code (ad, trailer end card, other).
- What “continue watching for free” unlocks vs the normal lock sheet.
