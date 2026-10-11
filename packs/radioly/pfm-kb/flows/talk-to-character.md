# Talk to a character

Participating modules: character-chat, show-details-and-unlock,
character-cards.

## Journey

1. Open a configured title (show page).
2. Eligible login sees a chat bubble (not the player character
   icons).
3. First visit: intro. Later: history for this login × character.
4. After five turns, feedback once. Crisis replies break character.

## User-Visible Invariants

- Guest: no bubble / no chat.
- Character cards on the player are a different surface.
- Progress on the title gates what the character may say.

## Failure modes

- No active character for the title → no chat, not a generic bot.
- Cap on dynamic bubble → hide bubble; do not show stale static
  copy.
