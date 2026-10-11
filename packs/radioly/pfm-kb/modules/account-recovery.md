# Account recovery

Aliases: forgot account, raise issue, find my account

## What It Is

The login path for a listener who cannot find their account. They file
a support request; they do **not** get an instant login. Distinct from
account-transfer (internal merge of two known ids).

## Actors

Listener on login (Android or iOS, recent enough app). Support reads
the ticket. Web is not eligible.

## Journey

1. Login shows “Forgot account?” when this path is offered.
2. Form: “Let’s find your account.”
   - Email (required)
   - One to four series they have listened to (required; search-to-add)
   - Payment transaction id (optional)
   - Short description (optional)
3. “Raise issue” opens a support ticket.
4. Success: request id, copy-to-clipboard, “Back to login.” Support
   email in the subtitle. Same device seeing the form again is told
   the request is already in progress.

## User-Visible Invariants

- This does not log them in or merge accounts.
- One request per device for a day; a repeat submit shows the existing
  request, not a second ticket.
- At most four series. Payment id and description are optional.
- Ineligible device or region: “not available,” not a blank form.

## Security / PII / Compliance

**Sensitive.** Email, device, series names, optional payment id, and
free-text description go to support.

- Identity for the request is the **device**, not a login they already
  have.
- Do not invent retention, lawful basis, or who may read the ticket.
- Do not log or echo payment ids in product copy beyond the form.

## Client Behavior

Needs network. Form copy and success sheet come from the server.
Closing success returns to login; it does not create a session.

## Event Meaning

Success is “we received your issue,” not “account restored.”
