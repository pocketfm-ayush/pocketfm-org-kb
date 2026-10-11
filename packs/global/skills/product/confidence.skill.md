<!-- How Groot scores a /groot run. Not an LLM feeling. -->
# Skill: Confidence score

**When:** `/groot` reaches `READY_FOR_CONFIDENCE`, or Slack asks why a run may
or may not open a PR.  
**Inputs:** Workflow `evidence` dict already collected.  
**Output:** Explain the score. Do not invent a number.

## What it is

Groot computes confidence in `groot/confidence/score.py`. Madeye must **not**
emit a substitute score. Bands decide whether finalize may open a draft PR.

| Band | Score | Meaning |
|---|---|---|
| ship-ready | ≥ 85 | Strong coverage; still needs human merge |
| ship-with-review | ≥ 70 | Draft PR allowed if new tests passed |
| needs-repair | ≥ 50 | Do not open a PR |
| blocked | < 50 | Do not open a PR |

`may_open_pr` is true only when `score >= 70` **and** `new_test_result == 1.0`.
A high score with failing new tests is still a no.

## Weights (do not change per request)

| Key | Weight | Evidence |
|---|---|---|
| `requirement_coverage` | 0.30 | `mapped_musts / total_musts` |
| `eval_integrity` | 0.20 | `evals_with_mutation / eval_count` (0 if no evals) |
| `new_test_result` | 0.25 | 1.0 if new tests passed, else 0.0. Pre-existing failures do not count. |
| `touch_point_completeness` | 0.15 | `covered_symbols / required_symbols` |
| `blast_radius` | 0.10 | 0 if path violation; 0.3 if new lint; 1.0 if lint known and clean; 0 if lint unknown |

Missing evidence keys score as 0. Residuals include unmapped MUSTs and failed new tests.

## What you may say

- Repeat the computed `score`, `band`, `breakdown`, `residual_risks`.
- Name which evidence key is holding the score down.
- Next action: add evals, map MUSTs, fix new tests, or stay blocked.

## Forbidden

- Inventing or rounding a "gut" confidence.
- Opening or promising a PR when `may_open_pr` is false.
- Blaming pre-existing failures for `new_test_result`.
- Changing weights because the feature "feels risky".
