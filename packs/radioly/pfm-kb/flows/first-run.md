# First run

Participating modules: onboarding-first-run, onboarding-show-pick,
trailer-code.

## Journey

1. Server decides first-run screens (name/age, gender, language,
   permissions / ATT).
2. Some new iOS US listeners get trailer-code (“remember the show
   code?”) instead of or beside the picker.
3. Everyone else: onboarding-show-pick (starter titles / trailers).
4. Hidden if they already answered, or (picker only) arrived on a real
   show link.

## User-Visible Invariants

- “Onboarding” in Slack may mean language, ATT, the title picker, or
  the show code. Ask which.
- Trailer-code is not the picker grid.
- Deep-linked new users skip the picker, not necessarily language or
  ATT.

## Failure modes

- Language options empty → do not invent a language list; hide or
  fall back as the server says.
- Unknown show code → miss copy, still let them reach the picker or
  Home.
- ATT / notification denied → continue first-run; do not block Home.
