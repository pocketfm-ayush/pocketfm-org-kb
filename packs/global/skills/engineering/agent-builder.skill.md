---
name: agent-builder
description: Design agents, skills, tools, and harness loops for reliable multi-step work.
triggers: [build agent, create skill, agent harness, tool design, subagent]
intent: implement
priority: 89
---

# 14 · Agent builder

**Job:** create agents/skills that constrain behavior usefully. See `agents-*`, `harness-*`, `role-*`, `mcp`.

## Do
1. One skill = one job; short triggers; explicit do/don't.
2. Wire intent → skill in the host (e.g. Groot `SKILL_FOR_INTENT`) when needed.
3. Prefer harness rechecks over longer prompts.
4. Tools: least privilege; no silent success on empty evidence.
5. Eval hooks (`eval`) for regressions in agent behavior.

## Do not
- One mega-skill that tries to do the whole tree.
- Duplicate AGENTS.md policy inside every skill — link it.

## Output
Agent/skill name · Triggers · Tools · Harness steps · Eval cases · Rollout
