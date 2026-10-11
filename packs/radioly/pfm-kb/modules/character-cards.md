# Player character cards

Aliases: character sheet, character icons, player characters

## What It Is

Icons (and a tooltip) on the **player** for a title that has a
published character sheet. Not the chat bubble.

## Actors

Listener on the player. CMS publishes the sheet.

## Journey

1. Player asks for this title’s character icons.
2. If the app vintage is too old, or there is no sheet, nothing shows.

## User-Visible Invariants

- Empty is normal when CMS has no sheet — do not invent characters.
- This is not Character chat.

## Client Behavior

Needs network. Android vintage gate.

## Gaps

Whether locale was meant to gate this is unresolved. The write /
approve path is a CS dashboard — not listener product.
