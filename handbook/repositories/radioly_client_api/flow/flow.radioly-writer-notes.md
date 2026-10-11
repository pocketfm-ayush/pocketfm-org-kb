---
id: flow.radioly-writer-notes
type: flow
repository: radioly_client_api
status: established
evidence:
  - radioly_client_api@95b5fafadad467aab75452e6d253cbface1f46c2:v2/content_api/services/ugc_note_service.py#ShowNoteService
---

**Aliases:** writer notes, note from the writer, UGC notes, episode note

**When to use:** A writer note on an originals title, label “NOTE FROM THE WRITER.” First stop `ShowNoteService`. Starts collapsed. No note means omit the block. Not a review and not a community post.

**Required inputs:** show or episode id and whether the note was missing or the reaction failed.
