---
name: agent
description: Run as a disciplined coding agent — loop, tools, evidence, and stop conditions.
triggers: [agent loop, run as agent, autonomous agent, agent behavior]
intent: implement
priority: 91
---

# Agent (runtime behavior)

**Job:** execute work with the harness, not one-shot guesses.

## Do
1. Start from `harness-intake` → plan → act → `harness-response-recheck`.
2. Load the smallest skill set for the task (see AI Dev Env index).
3. Use tools for evidence; refuse silent empty successes.
4. Stop when success criteria met or blocker needs a human.
5. Prefer sub-skills (`debugger`, `test-engineer`, …) over improvising policy.

## Do not
- Infinite tool loops without progress.
- Skip security/deploy gates on prod-adjacent work.

## Related
`harness-loop`, `agent-builder`, `mcp`, `eval`, roles under `role-*`
