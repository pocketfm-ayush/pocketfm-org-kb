# Default home onboarding shows

## Journey
1. Caller sends platform/locale/language/gender headers.
2. Default home service loads onboarding feed configuration.
3. Ranked show ids/objects return for home bootstrap modules.

## Modules
- [default-home-feed](../modules/default-home-feed.md)
- [show-catalog-read](../modules/show-catalog-read.md)

## Failure modes
- Invalid/missing audience headers → bad request.
- Empty CMS feed config → empty show list.
