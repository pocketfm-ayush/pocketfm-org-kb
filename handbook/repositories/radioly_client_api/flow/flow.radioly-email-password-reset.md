---
id: flow.radioly-email-password-reset
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/user_api/views.py#password_reset_email
---

**Aliases:** forgot password, password reset, reset email

**When to use:** Email-login password reset. First stop `password_reset_email`. An email opens the reset screen. Not phone OTP login and not forgot-account recovery.

**Required inputs:** email login and whether the reset mail arrived.
