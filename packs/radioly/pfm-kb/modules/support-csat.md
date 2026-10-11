# Support CSAT

Aliases: ticket rating, support satisfaction, CSAT

## What It Is

After a **support ticket**, they rate the experience: happy or
unhappy, optional short comment. Not Help’s “was this helpful.”
Not the app-rating popup.

## Actors

Listener on a recent enough app (login required). Support
already has the ticket.

## Journey

1. They submit happy or unhappy, optional comment.
2. Too-old app: “not supported,” not a silent drop.
3. Success: “Feedback submitted.”

## User-Visible Invariants

- Rating is only happy / unhappy. Do not invent a 1–5 scale.
- This does not close or reopen the ticket on screen.

## Client Behavior

Needs network and a login. Failure to send is a visible miss,
not a Help-article miss.

## Security / PII / Compliance

**Sensitive.** Ticket id, rating, and comment go to support.

- Do not invent retention.
- Do not echo ticket ids in product copy beyond this screen.
