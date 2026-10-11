# OTP login

Aliases: login, phone login, email OTP, skip login, guest

## What It Is

How a listener starts a **session**: phone or email code, or Google /
Apple, or skip (guest). This is **not** “Forgot account?” (that is
account-recovery) and **not** the 48-hour invite code for a family
profile (that is multi-profile).

## Actors

Listener on the login screen (app; methods vary by market and vintage).
Guest is the same person with no login — identity is the device.

## Journey

1. Server says which methods to show (phone, email, Google, Apple,
   skip). Do not invent the list.
2. Phone or email: they ask for a code, then enter it.
3. Correct code continues the login. Wrong or expired code stays on
   the screen.
4. Skip leaves them as guest. Library and progress fall back to the
   device (same rule as those modules).
5. “Forgot account?” is a ticket, not a session.

Changing the phone on an existing login is a **second** code path
(old number, then new). It is not a new signup.

## User-Visible Invariants

- Success here is a session. Account-recovery success is “we got your
  issue.”
- Invite / family-profile codes are not this login code.
- Too many send or verify tries: “try again later,” not a blank login.
- Expired code asks them to request a new one. Wrong code does not.
- India Android is phone-first in the default list; other markets lean
  email / Google / Apple. Tests can add phone or hide email — treat
  the live list as server-owned.

## Client Behavior

Needs network. A code that was never verified does not create a
session. Guest does not keep another person’s library.

## Security / PII / Compliance

**Sensitive.** Phone, email, and the one-time code.

- Do not echo the full phone or email in logs or product copy.
- Do not invent retention or lawful basis for the code.

## Gaps

- Whether a follow-on identity step (beyond “code is correct”) is
  required before Home.
- Which login-method test is live.
- Email password reset is a separate product (email-password-reset).
- Whether Google / Apple sign-in hits the weekly device-login cap
  is a gap on device-login-limit.
