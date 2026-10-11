# UGC backend writer bridge

Aliases: writer achievements sync, ugc profile state

## What It Is
Radioly calls the creator/UGC backend so writer achievements and writer flags
can appear on profile, and so deleting an FM account also cleans up creator-side
identity.

## Actors
Writer / aspiring writer. Listener viewing writer profile. Account-delete flow.

## Journey
1. Profile needs writer state → Radioly fetches profile-state from UGC backend.
2. On FM account delete → Radioly notifies UGC to delete/sync creator user.

## User-Visible Invariants
- Stage/Studio UI is separate ([stage](stage.md)); this is the backend bridge.
- Related: [writer-profile](writer-profile.md), [account-delete](account-delete.md).

## Security / PII / Compliance
Uses service credentials — never commit or log them.
