# Subscriptions

Aliases: subscription, premium pass, VIP, cancelled but valid, grace

## What It Is

The pass the listener **owns** after they pay — not the buy sheet.
Paywall chooses what to show; this module is whether they still have
access, and for how long.

## Actors

Logged-in listener. Store / billing gateway reports renew, cancel, and
pause. The app does not flip “subscribed” on its own.

## Journey

1. Listener picks a plan the server already offered on the sheet.
2. Billing confirms; the pass becomes active (or pending, then active).
3. Cancel or pause can still leave access until the stated end
   (cancelled-but-valid, paused-but-valid).
4. After the end date, most passes get a retry window (grace). Access
   is computed with an extra day after the stated end.
5. Some no-mandate plans skip grace and expire when the date passes.
6. After about a week past the end, some listeners lose premium while
   billing is still retrying. That is not the same as still-valid grace.

## User-Visible Invariants

- Cancelled today is not “locked today” if they are still in a valid
  window.
- India grace is 60 days; US (and unknown markets) is 30. Do not use
  one number everywhere.
- Retired plans are not sold to new buyers. People already on them
  keep them.
- Do not invent plan prices, plan IDs, or experiment splits.

## Client Behavior

Needs network and a login. History and “am I subscribed?” follow the
login, not a user id the app stuffed in.

## Gaps

Which pass family or experiment is live now is not recorded here.
