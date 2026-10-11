<!-- After planner — adversarial plan review. -->
# Skill: Harness plan critique

**When:** After `role-planner` produces a plan; before implementation.
**Roles:** act as plan-checker + adversary (Codex `plan-checker`, gstack reviews).

## Checklist

- [ ] Every task has acceptance criteria + validation command
- [ ] Dependencies (`depends_on`) acyclic and complete
- [ ] Allowed/protected paths respected
- [ ] Missing research called out (no silent TBD on load-bearing facts)
- [ ] Security / data-migration / rollback considered when relevant
- [ ] Test plan covers happy path + one failure path
- [ ] Deploy/monitoring tasks present if shipping

## Output

Severity tags only (do not rewrite the plan inline unless asked):

- **Blocker** — must fix before implement  
- **Suggestion** — should fix  
- **Nit** — optional  
- **Question** — needs human/researcher  

`PLAN_CRITIQUE: PASS | FAIL` — FAIL if any Blocker remains.
