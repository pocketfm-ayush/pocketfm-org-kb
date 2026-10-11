# Story evolution

Aliases: story cards, collectible cards, vault, archive

## What It Is

Collectible cards earned by finishing episodes of an **enabled** title.
Home, show, player, profile, and library can surface a banner or vault
entry. The vault is the collection.

## Actors

Logged-in listener in the test. Default: iOS; US or India; not
brand-new on the device; already listening that title. Guest: no vault.

## Journey

1. They listen most of an episode (server can raise the bar).
2. A card unlocks (character or event; rarity tags).
3. Banner / bottom sheet: “view your card” / “view collection.”
4. Vault: unlocked, locked, coming soon. Share a card. Continue
   listening from resume.
5. Completing the set can show archive-complete copy.

## User-Visible Invariants

- Cards are per enabled title, not a global sticker book.
- Profile / library show a quiet vault entry, not the same banners as
  Home or player.
- Do not invent which titles or how many cards are live.
- Not interactive-story branches and not Gift & Earn.

## Client Behavior

Needs network and a login. Opening the vault counts as viewed.
Impression caps on banners are server-owned.

## Event Meaning

Banner seen/tapped, vault opened, card viewed, share, continue — used
to know they engaged the collection, not that they paid.

## Gaps

- Which titles are collectible.
- Live impression / “just earned” caps.
