# Merchandise giveaway

Aliases: giveaway, merch giveaway, MVS giveaway, bottom slider gift

## What It Is

A merch entry form for listeners **already on a campaign** — not coins,
not cashback, not a store.

## Actors

Logged-in listener who was assigned a campaign. Campaign ops can close
it (inactive, expired, or target reached).

## Journey

1. Eligible listeners may see a Home slider (capped: 2/day, 3/week,
   5 lifetime per campaign).
2. They open a web form and submit name, email, phone, address,
   optional shirt size, and consent.
3. One entry per campaign. Already submitted → not eligible.

## User-Visible Invariants

- The app cannot enter someone who was never assigned.
- Closed campaign → no slider, no submit.
- This is not a coin or wallet credit.

## Security / PII / Compliance

Collects contact and shipping data plus consent. Treat as sensitive.
Do not log raw addresses or phone numbers in product copy.

## Client Behavior

Needs network and a login. Slider absence is a valid “not eligible /
already entered / cap hit” state.
