# In-app support ticket

Aliases: support chat, contact support, raise a ticket

## What It Is

In-app **chat → support ticket**. Not Help articles. Not
“Forgot account?” (account-recovery).

## Actors

Listener in the app. Support reads the ticket.

## Journey

1. They open support chat (typically Profile → Support).
2. Form: name (required), phone **or** email (one required),
   description.
3. Submit opens a ticket. Success returns the ticket the
   support tool created.

## User-Visible Invariants

- This does not log them in or restore an account.
- Missing name, or missing both phone and email, stays on the
  form.
- Do not reuse the forgot-account series/payment form here.

## Client Behavior

Needs network and a session.

## Security / PII / Compliance

**Sensitive.** Name, phone, email, and free-text description
go to support.

- Do not invent retention or who may read the ticket.
- Do not log the full phone or email in product copy.
