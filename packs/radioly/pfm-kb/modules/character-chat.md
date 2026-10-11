# Character chat

Aliases: talk to character, character chatbot, show character chat

## What It Is

A logged-in chat with one in-world character from a configured title.
The character only knows episodes the listener has reached.

## Actors

Logged-in listener. Guest cannot open chat. Only titles with an
active character config.

## Journey

1. Show page may show a character bubble (eligible + configured title).
2. First visit: intro (and intro video at most once ever).
3. Later turns stream a reply. History is this login × this character.
4. After five turns, a feedback sheet can show **once** for that
   character. The conversation may be sent with the feedback.
5. Dynamic bubble text after five turns; at most one impression per
   day / week / year. Hit the cap → hide the bubble (do not fall back
   to static copy).

## User-Visible Invariants

- Login required. History is account-scoped.
- No spoilers past the listener’s furthest episode.
- Self-harm / crisis: drop character and point to real helplines.
  Do not stay in-story.
- Disclose that this is AI, not a real person.
- Some US time zones are excluded from enrollment (unless the login
  is already allowlisted).
- Enrollment also needs recent listen time on a configured title,
  and a device that is not brand new.

## Security / PII / Compliance

Treat chat text as sensitive. Feedback explicitly shares the thread.

## Client Behavior

Needs network and a login. Empty opener is allowed only on first
visit. Message cap is 500 characters.

## Gaps

Which titles/characters are live, and which chat-style tests are on,
are not recorded here.
