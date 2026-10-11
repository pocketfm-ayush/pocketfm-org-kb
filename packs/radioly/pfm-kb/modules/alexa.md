# Alexa

Aliases: Alexa, Pocket FM skill, voice command

## What It Is

Voice play / resume / next / previous / start-over / play episode N,
plus “unlock next” with coins and “recommend a series.”

## Actors

Alexa listener. Device is enough to **play**. Coin unlock needs a
login.

## Journey

1. Skill sends the command (body language wins over the header).
2. Play uses last-listened on this show; if that episode is fully
   finished, advance to the next. Title can be resolved by search.
3. Locked next episode: ask to unlock with coins, or say there are
   not enough coins, or ask them to log in.
4. Unlock deducts coins for **one** episode, then resumes. Spoken
   confirm can include the episode and coin amount.
5. Unknown / failed command → recommend.
6. Audio links are time-limited.

## User-Visible Invariants

- Guest can resume; guest cannot spend coins.
- VIP can hear locked episodes without the coin prompt.
- Do not invent prices. Insufficient balance is spoken, not a
  mobile paywall sheet.

## Client Behavior

Needs network. Bad token → “Invalid Token.”

## Gaps

Which recommend titles are current, and skill-side utterance
mapping, are not recorded here.
