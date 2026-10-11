---
name: api-design
description: Design or review HTTP/RPC contracts — resources, errors, versioning, idempotency.
triggers: [api design, endpoint design, REST, RPC contract, OpenAPI]
intent: plan
priority: 86
---

# 11 · API design

**Job:** define clear, stable contracts between clients and services.

## Do
1. Name resources and actions; keep URLs/methods consistent with existing APIs.
2. Specify request/response shapes, error envelope, and status codes.
3. Authn/z and tenancy fields explicit.
4. Idempotency keys for unsafe retries; pagination/filter conventions.
5. Compatibility: additive changes preferred; document breaking changes.

## Do not
- Expose internal table shapes as the public API without a DTO boundary.
- Return 200 for domain failures if the repo standard uses problem statuses.

## Output
Endpoints · Schemas · Errors · Auth · Compatibility notes · Test cases
