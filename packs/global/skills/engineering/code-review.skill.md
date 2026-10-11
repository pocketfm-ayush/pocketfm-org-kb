---
name: code-review
description: Review diffs for correctness, regressions, style fit, and missing tests — not nitpick theater.
triggers: [code review, review this PR, review diff, look at this change]
intent: review
priority: 90
---

# 04 · Code review

**Job:** find real defects and missing proof. Compose with `role-reviewer` +
`harness-review-recheck`. Groot also attaches the pack's language stack skill
(`python` / `golang` / `kotlin` / …) and any pack overlay of this file
(`<pack>/skills/code-review.skill.md`).

## Do
1. Read the PR intent first, then the diff.
2. Prioritize: correctness → data safety → authz → regressions → tests → style.
3. Apply **repo/language lenses** from attached stack + pack `code-review` overlays.
4. Cite file/symbol for every finding; include a concrete better approach.
5. Separate blocking vs non-blocking.
6. Ask for missing tests or evidence when behavior changed.

## Do not
- Rewrite the author's approach unless it is unsafe or inconsistent with repo norms.
- Apply another pack's patterns (e.g. radioly ORM rules inside pocket_search).
- Approve without checking tests / CI when the change is behavioral.
- Flood with optional renames.

## Output
Summary · Blocking · Non-blocking · Test gaps · Better approaches · Verdict
