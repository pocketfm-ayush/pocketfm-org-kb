# Login

Participating modules: otp-login, email-password-reset, device-login-limit,
account-recovery, onboarding-first-run, multi-profile.

## Journey

1. Server lists methods (phone, email, Google, Apple, skip).
2. Phone / email: send code → enter code → session.
3. Skip → guest (device identity). Google / Apple → session if offered.
4. After a new session, first-run screens may still run
   (onboarding-first-run).
5. “Forgot account?” is account-recovery. It does **not** mint a
   session.

## User-Visible Invariants

- Login code ≠ recovery ticket ≠ 48-hour family-profile invite.
- Signing in on a deactivated login lifts the pause
  (account-deactivate).
- Signing in on a deleted login can undo the delete request
  (account-delete); name may show as “PocketFM User.”

## Failure modes

- No phone or email on the request and none on the device → ask for
  one; do not invent a destination.
- Rate limit → try later; do not open recovery.
- Weekly device-login cap → “too many devices,” not “account not
  found.” Email password reset is not this code path.
- Expired code → request a new one. Wrong code → stay on verify.
- Invitee code / deleted family slot → multi-profile errors, not
  “account not found.”
