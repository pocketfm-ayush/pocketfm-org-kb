---
name: security-review
description: Threat-model the change — authn/z, secrets, injection, SSRF, data exposure.
triggers: [security review, threat model, authz, secrets, vulnerability]
intent: review
priority: 93
---

# 08 · Security review

**Job:** find abuse paths. Align with `agents-security` and `role-adversary`.

## Do
1. Identify trust boundaries and who can call what.
2. Check authn, authz, tenancy, and IDOR-class access.
3. Secrets: no plaintext in repo/logs; ExternalSecret / vault patterns for deploy.
4. Input validation, injection (SQL/NoSQL/command), SSRF, path traversal.
5. Data leaving the boundary (PII in logs, over-fetch APIs).

## Do not
- Rubber-stamp “looks fine” without stating what was checked.
- Demand rewrites for theoretical issues with no path to exploit when severity is low — still note them.

## Output
Assets · Threats · Findings (sev) · Mitigations · Residual risk
