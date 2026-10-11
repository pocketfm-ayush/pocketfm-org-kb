# Device login limit

Aliases: weekly device login limit, too many devices

## What It Is

A **weekly cap on distinct devices** that may request a login
code for one login. Distinct from multi-profile’s “five devices
at once” listen/download benefit, and from OTP rate limits.

## Actors

Listener asking for a phone/email code. Ops can exempt one login
(internal). The listener never sees that exemption screen.

## Journey

1. They ask for a login code on this device.
2. This device already used this week → code may send.
3. A new device, and **five** other devices already logged in
   during the last **seven** days → blocked: “You’ve reached the
   weekly device login limit.”
4. Exempted login: the cap does not apply.

## User-Visible Invariants

- Five unique devices per rolling week, not five simultaneous
  players.
- Same device can come back. A sixth *new* device cannot.
- This is not “account not found” and not a family-profile cap.

## Client Behavior

Needs network. The block is on **send code**, before a session.

## Security / PII / Compliance

**Sensitive.** Login + which devices signed in this week.

- Do not invent retention of the device list.
- Exemption is ops-only. Do not expose it as a listener toggle.

## Gaps

Whether the same cap applies to Google / Apple sign-in (not only
code send) is not recorded here.
