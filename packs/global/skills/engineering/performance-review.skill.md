---
name: performance-review
description: Find latency, throughput, and cost issues — hot paths, N+1, cache, payload size.
triggers: [performance, slow, latency, optimize, N+1, throughput]
intent: review
priority: 84
---

# 09 · Performance review

**Job:** locate real hotspots with evidence, not micro-optimizations.

## Do
1. Define the SLO / user-visible symptom (p95, timeout, cost).
2. Find the hot path (trace, query plan, profile, RED metrics).
3. Check N+1, missing indexes, unbounded scans, chatty RPCs, large payloads.
4. Cache/invalidation correctness before “just add Redis”.
5. Prefer measured before/after.

## Do not
- Optimize cold paths.
- Add caching that can serve stale authz or money-critical state without a plan.

## Output
Symptom · Hot path · Bottleneck · Options · Recommended change · How to measure
