# Listener profile

Aliases: my profile, edit profile, profile page, profile details

## What It Is

The **person page**: name, photo, language, gender, bio, and (when
opened) that person’s titles. Edit is the same facts after first-run.

Not multi-profile (family slots), not community posts (community-updates),
not first-run name/gender/language screens (onboarding-first-run).

## Actors

Listener viewing self or someone else. Only the owner can edit.

## Journey

1. Open profile (self or another login).
2. Self: name, photo, gender, language, bio, optional social links.
3. Another person: public card and titles — not their private library.
4. First-run already collected name / gender / language; this is the
   later edit and the public view.

## User-Visible Invariants

- You cannot edit another login by sending their id.
- Phone numbers must not appear on people cards (same as
  community-updates).
- Multi-profile: India can show the **chosen slot’s** name / photo /
  language on this page. Other markets: do not assume that swap.

## Client Behavior

Needs network. Edit persists on the login (or slot). Empty bio is
empty, not a failed Home.

## Security / PII / Compliance

**Sensitive.** Name, age / date of birth, gender, language, photo,
bio, social links.

- Do not invent what others can see beyond the public card.
- Profile “verification / completion” extras are test-gated — do not
  treat them as always on.

## Gaps

- Live public fields vs owner-only fields.
- Whether age is editable after first-run in every market.
