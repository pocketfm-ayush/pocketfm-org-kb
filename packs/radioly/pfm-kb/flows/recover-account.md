# Recover account

Participating modules: account-recovery.

## Journey

1. Login shows “Forgot account?” when recovery is offered.
2. Form (email + 1–4 series; optional payment id and note).
3. Ticket filed. Success shows a request id and back-to-login.
4. Same device, same day: already-in-progress, no second ticket.
5. Support works the ticket. This flow does **not** merge accounts
   (that is account-transfer).

## User-Visible Invariants

- Success means “we got it,” not “you are logged in.”
- Web and old apps do not get this path.

## Failure modes

- Support ticket create fails → try-again error; no request id.
- Ineligible → “not available,” not a broken login.
