# Email password reset

Aliases: forgot password, reset password, change password

## What It Is

How a listener with an **email login** resets that password. An
email opens a reset screen in the app. This is **not** OTP login
and **not** “Forgot account?” (account-recovery).

## Actors

Listener who knows the email on the login. No session is required
to request the mail.

## Journey

1. They enter the email.
2. Unknown email: “enter a valid email.” No mail.
3. Known email: reset mail (from care). A still-valid link is
   reused; it is not a new one every tap.
4. They open the link in the app, type password twice.
5. Mismatch stays on the screen. Expired or used-up link: request
   a new mail.
6. Success: password changed, confirmation mail, path back to Home.

## User-Visible Invariants

- Success here is a new password, not a session and not a support
  ticket.
- The link expires (about an hour).
- Do not treat this as phone OTP.

## Client Behavior

Needs network. The mail must be opened; pasting a password in the
app without the link does not reset.

## Security / PII / Compliance

**Sensitive.** Email and the new password.

- Unknown-email copy reveals that the address is not on a login.
- Do not echo the password or the full email in logs or product
  copy.
- Do not invent retention.

## Gaps

Whether every market still shows this next to OTP, and whether
web (not the app link) can complete the reset, are not recorded
here.
