# No-ad pack

Aliases: ad-free pack, go ad-free, no ads days

## What It Is

A time-boxed purchase that turns off **network mid-roll** and **most promotional first-party player clips** for a number of days. It is not a subscription, not unlock, and not a banner-off guarantee.

## Actors

Logged-in listener. Days remaining and whether they can be sold another pack are server-owned.

## Journey

1. App asks whether they can buy and how many days are left.
2. After pay, the app records the granted days.
3. Later checks use **now**, not the purchase moment, to decide if the pack is still on.

## User-Visible Invariants

- Days left is what the listener sees. Expiry is evaluated at check time.
- This does **not** turn off AI-voice warnings, explicit-content disclaimers, or watch-to-unlock / earn-coins.
- Display ads can still appear under a test.
- A “go ad-free” prompt can appear on mid-rolls for eligible app vintages — do not show it on unrelated legal/UX clips.
- Days granted from a purchase amount and market are server-owned. Do not hardcode prices or day slabs.

## Client Behavior

Needs network and a logged-in user. Closing pay without a recorded grant leaves ads on.

## Security / PII / Compliance

Status is for the authenticated listener only. Do not infer ad-free from a device that is logged out.

## Gaps

Whether a second purchase extends, replaces, or stacks days is not evidenced here.
