<!-- After reviewer — blockers must clear; PR tools verified. -->
# Skill: Harness review recheck

**When:** After `role-reviewer` (or Bugbot/security review), before finishing.

Before REVIEW: APPROVE / REQUEST_CHANGES:

1. If a PR URL was in the ask, confirm `fetch_pr` ran (or cite why it failed).
2. Read PRIOR ROLE outputs; check claims against `/repo/` + tools + PR patches.
3. Blockers only for wrong/missing evidence, broken contracts, or unsafe changes —
   not style nits.
4. Every Blocker / Suggestion has path (+ line) and a concrete better approach.
5. Verdict must be REVIEW: APPROVE or REVIEW: REQUEST_CHANGES with blocker count.
6. List what you checked (paths, tools). No rubber-stamp LGTM.
7. Call `post_pr_review` only when the user asked to post GitHub comments —
   and only after the Slack ANSWER shape is ready.

`REVIEW_RECHECK: PASS | FAIL`.
