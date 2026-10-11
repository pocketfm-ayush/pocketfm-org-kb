# Skill: Role — Planner

**When:** User asks to plan, break down, outline sprints/tasks, or `/plan`.
**Not for:** Jumping straight to code without intake.

## Process

### 0. Intake
Run `harness-intake`. Clarify goals, scope, env, risks.

### 1. Research (light)
Spawn or follow `role-researcher` / `role-scout` for architecture, similar code,
pack CONTRACT. Do not invent names.

### 2. Plan structure
- Overview & approach  
- Sprints/phases  
- Atomic tasks with: owner role, `depends_on`, acceptance criteria, **validation command**  
- Risks & rollbacks  
- Test & deploy/monitoring notes  

### 3. Critique
Hand off to `harness-plan-critique` before implement.

## Rules

- Prefer questions over silent defaults.
- Mark ASSUMPTION explicitly.
- No task without a way to verify it.
- End with `PLAN: READY_FOR_CRITIQUE` or `PLAN: BLOCKED (questions)`.
