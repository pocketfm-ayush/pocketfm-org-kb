# Email password reset

Aliases: password reset, forgot password, reset email

Product context: `radioly/pfm-kb/modules/email-password-reset.md`

## What it is

Email-based password reset for credential accounts (not OTP login).

## Graph anchors

CODE SEARCH `password_reset` / `forgot_password` under user / email modules.


## Key product notes

How a listener with an **email login** resets that password. An
email opens a reset screen in the app. This is **not** OTP login
and **not** “Forgot account?” (account-recovery).

## Risks

- Mixing with OTP login flow.

## Query

```bash
GRAPH=radioly/graphify/graphify-out/graph.json
graphify query "email password reset" --graph $GRAPH --budget 2000
```

Verify symbols via CODE SEARCH before answering. Graphify is discovery only.

