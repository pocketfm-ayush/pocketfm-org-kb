# Onboarding to home

## Journey
1. New listener hits auth/onboarding.
2. Completes OTP/email/password and optional profile details.
3. Shell routes into home tabs/feed.

## Modules
- [auth-and-onboarding](../modules/auth-and-onboarding.md)
- [app-start-and-shell](../modules/app-start-and-shell.md)
- [home-feed-discover](../modules/home-feed-discover.md)

## Failure modes
- Auth config/GDPR gates block progress without clear retry.
- Guest vs logged-in misclassification loops splash.
