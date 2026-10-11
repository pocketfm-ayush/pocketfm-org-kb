<!-- Convert a free-form PRD into prd-format. Do not analyse readiness. -->
# Skill: Normalize PRD

**When:** User says convert / normalize / reformat / rewrite a PRD, or `/groot`
has a raw Confluence / Google Doc / PDF / Slack paste.  
**Inputs:** Raw PRD text, optional pack `CONTRACT.md` + feature overviews.  
**Output:** One markdown document that matches `prd-format.skill.md`. Nothing else.

## Standard

Be a clerk, not a product owner. Move facts. Do not improve the idea. Do not
decide open questions. Do not add MUST lines that were not in the source.

## Procedure

1. Read `prd-format`. Emit every required heading in that order.
2. Copy each fact into the matching section. Keep the author's meaning.
3. Split compound requirements into `MUST-1`, `MUST-2`, … `SHOULD-*`.
   If the source already numbered them, keep those IDs.
4. Put anything that is a question, TBD, or "we should decide" under
   `## Open questions`. Do not answer them.
5. Copy `## Current behavior` from the source PRD when it has any. If a pack
   is attached, add only pack names that already appear in that text or in the
   pack; do not replace the author's description. If the source is silent:
   pack names when a pack is attached, else `unknown`.
6. If two sentences conflict, put both in the section and add an Open question
   quoting both. Do not pick a side.
7. If a section has no source text, write `unknown`.

## Forbidden

- Inventing eligibility, cache keys, endpoints, metrics, or rollout.
- Dropping a required heading.
- Turning this into PRD analysis (no JSON, no P0 questions, no readiness).
- Turning this into implementation.

## Slack / chat

If the user only asked to convert, return the normalized markdown.
If they also asked to analyse, normalize first, then stop and say the next
step is `prd-analysis` on this normalized body.
