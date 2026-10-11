# Notification permission prompts

Aliases: enable notifications, notification sheet, push opt-in

## What It Is

In-session **Allow notifications** sheets (copy + a few show images).
Not an inbox. Not first-run ATT / notification (that is
onboarding-first-run).

## Actors

Listener who has not already allowed. Server owns whether to show.

## Journey

1. App asks after last unlock, a purchase, app open, or a show page
   they are already into.
2. Already allowed → no sheet.
3. Each trigger is capped so it does not keep asking.
4. Android 13+ can show an extra system-permission sheet.
5. Brand-new iOS device: no app-open sheet in the first hour.

## User-Visible Invariants

- No images → do not invent a sheet.
- “Not eligible” is quiet skip, not a failed Home.
- Do not treat this as a notification feed.

## Client Behavior

Needs network. Deny / later must not block listening.

## Gaps

Which copy variant is live, and whether Android shows a first-run
sheet outside tests, are not recorded here.
