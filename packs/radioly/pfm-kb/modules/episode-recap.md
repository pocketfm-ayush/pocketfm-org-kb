# Episode recap

Aliases: episode recap, recap audio, story recap

## What It Is

A short **audio recap for one episode**. Not the show-level AI recap
and not a new episode in the season.

## Actors

Listener opening an episode that has a recap on file.

## Journey

1. App asks for that episode’s recap.
2. If none exists, the listener sees not-found — do not invent a recap.

## User-Visible Invariants

- Show-level AI recap is a different product. Ask which one.
- A recap card is not an extra numbered episode.

## Client Behavior

Needs network. Missing recap fails visibly.
