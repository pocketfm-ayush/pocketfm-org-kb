# App rating popup

Aliases: feedback popup, rate the app, store rating sheet

## What It Is

An in-app **rate Pocket FM** sheet (emoji / stars). High scores
can send them to the store. Not the player-minimise NPS survey
(user-survey). Not Support CSAT.

## Actors

Logged-in listener the server already marked as eligible.
Server owns whether it may show.

## Journey

1. Eligible open (or a Home overlay) shows the sheet.
2. Skip: hidden for about six days.
3. Rate: low/mid can take a typed comment; high can open Play
   Store or App Store.
4. Thank-you, then back to listening.
5. After a rating, next ask waits about six or nine days. After
   five ratings, it stops.

## User-Visible Invariants

- This is not the NPS form. Do not reuse those questions.
- Closing without a score is a skip, not a 1-star.
- Do not invent when they were first enrolled.

## Client Behavior

Needs network and a login. Store redirect is device/store, not
a Pocket FM page.

## Security / PII / Compliance

Rating and optional review are tied to the login. Do not invent
retention or store-sharing rules.

## Event Meaning

A store tap is “they left to rate,” not a completed store
review.

## Gaps

Who first enrolls a login, and which Home overlay wins when this
and another campaign compete, are not recorded here.
