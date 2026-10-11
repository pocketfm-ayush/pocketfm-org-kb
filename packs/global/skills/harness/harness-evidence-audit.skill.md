<!-- After research — every claim needs evidence. -->
# Skill: Harness evidence audit

**When:** After researcher/scout; before trusting a brief as ground truth.

## Rules

- Each factual claim → `path`, `tool`, `URL`, or `INFERRED`.
- Contradictions between sources → call out; prefer newer tool/code evidence.
- KB/AGENTS.md alone is insufficient for runtime claims (latency, deploy state).
- Truncated tool payloads → incomplete; narrow and retry.

## Output

Table or bullets: Claim | Evidence | Status (OK|WEAK|MISSING).  
`EVIDENCE_AUDIT: PASS` only if no MISSING on load-bearing claims.
