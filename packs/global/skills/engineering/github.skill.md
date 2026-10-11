---
name: github
description: Branch, commit, PR, review, and CI hygiene for GitHub-hosted repos.
triggers: [github, pull request, open PR, branch, CI, gh]
intent: implement
priority: 82
---

# 13 · GitHub

**Job:** ship through GitHub cleanly. Align with `agents-git` and `agents-pr`.

## Do
1. Branch from the right base; name with ticket id when required.
2. Commits: why over what; no secrets.
3. PRs: summary, test plan, link ticket; keep scope tight.
4. Respect CI — fix failures, do not skip hooks unless explicitly asked.
5. Use `gh` for PR/issue operations when available.

## Do not
- Force-push shared main/master.
- Open mega-PRs that mix unrelated concerns.
- Commit `.env` / credentials.

## Output
Branch · Commits · PR body checklist · CI status · Follow-ups
